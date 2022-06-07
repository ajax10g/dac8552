import sys
from time import sleep

from dac8552 import DAC8552, DAC_A, DAC_B, MODE_POWER_DOWN_100K

# STEP 1: Initialise DAC object:
dac = DAC8552()
