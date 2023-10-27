#!/usr/bin/env python3

# from the python-constraint package
import constraint
from pprint import pprint

# All frequencies in MHz
platform = 'xilinx'
fin     = 50
fout    = 107.386350
error_threshold = 0.1
period = 1.0 / (fin * 1e6) * 1e9
print(f"platform: {platform} fin: {fin}MHz ({period} ns) fout: {fout}MHz, error_threshold: {error_threshold}")

if platform == 'altera':
    vco_min  = 600
    vco_max  = 1300
    max_mult = 200
    max_div  = 400
elif platform == 'xilinx':
    vco_min = 800
    vco_max = 1600
    max_mult = 64
    max_div = 128
elif platform == 'xilinx-mmcm':
    vco_min = 600
    vco_max = 1200
    max_mult = 64
    max_div = 128 * 128

problem = constraint.Problem()
problem.addVariable('mult', range(1, max_mult))
problem.addVariable('div', range(1, max_div))

def vco_range(mult):
    vco_freq = fin * mult
    return vco_min <= vco_freq and vco_freq <= vco_max

def relative_error(mult, div):
    return abs((fin * mult / div - fout)) / fout

def is_precise(mult, div):
    return relative_error(mult, div) < error_threshold

problem.addConstraint(vco_range, ['mult'])
problem.addConstraint(is_precise, ['mult', 'div'])
solutions = problem.getSolutions()
errors = [relative_error(s['mult'], s['div']) for s in solutions]
solutions_by_error = list(zip(errors, solutions))

def sort_by_error(tuple):
    return tuple[0]

solutions_by_error.sort(key=sort_by_error)
pprint(solutions_by_error)
