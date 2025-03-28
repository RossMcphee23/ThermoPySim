import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from systems.ideal_gas import IdealGas
from systems.van_der_waals_gas import VanDerWaalsGas


def test_ideal_gas_law():
    gas = IdealGas(pressure=101325, volume=0.0224, temperature=273, moles=1)
    assert gas.state_equation()  # This should now pass

def test_van_der_waals_state_equation():
    #Initialised parameters
    pressure = 100000 #Pascals
    volume = 0.025 #m3
    temperature = 300 #K
    moles = 1 # number of moles
    a = 0.364 # L^2 bar /mol^2
    b = 0.0427 # L/mol 

    #conversion of units potentiality??
