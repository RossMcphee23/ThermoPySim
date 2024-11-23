import math
from .base_system import ThermodynamicSystem

class IdealGas(ThermodynamicSystem):
    def state_equation(self):
        # Ideal gas law: PV = nRT
        R = 8.314  # Universal gas constant in J/(mol·K)
        calculated_pressure = (self.moles * R * self.temperature) / self.volume
        
        # Debugging output
        print(f"Given Pressure: {self.pressure}, Calculated Pressure: {calculated_pressure}")
        
        # Adjust relative tolerance to handle floating-point imprecision
        return math.isclose(self.pressure, calculated_pressure, rel_tol=1e-3)

