import sys
import os
import pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from engines.carnot_engine import CarnotEngine

def test_carnot_efficiency():
    engine = CarnotEngine(hot_temp=500, cold_temp=300)
    assert engine.efficiency() == pytest.approx(0.4, rel=1e-2)

'''
TESTING NEW FILE
'''