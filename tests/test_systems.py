import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from systems.ideal_gas import IdealGas

def test_ideal_gas_law():
    gas = IdealGas(pressure=101325, volume=0.0224, temperature=273, moles=1)
    assert gas.state_equation()  # This should now pass


