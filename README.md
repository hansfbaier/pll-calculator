This script helps with calculating the best multiplication / division 
factors for Altera/Xilinx FPGA PLLs.

Currently it lacks any UI (even a command line UI).
So the way to use it is:
Edit the desired PLL parameters in the script, for example:
```
platform = 'xilinx'
fin     = 50
fout    = 107.386350
```

and then run the script:
```
$ python3 pll-calc.py
```

It will output available options for the multipliers/dividers,
sorted by the least amount of error (deviation) from the
desired target frequency.

In order to run this script, the python-constraint package
needs to be installed:
```
pip install python-constraint
```
