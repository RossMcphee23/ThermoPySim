from .base_system import ThermodynamicSystem

class VanDerWaalsGas(ThermodynamicSystem):
    def __init__(self, pressure, volume, temperature, moles, a, b):
        super().__init__(pressure, volume, temperature, moles)
        self.a = a #Attraction
        self.b = b #Volume exclusion
    def state_equation(self):
        R = 8.314 # universal gas constant
        term1 = (self.pressure + (self.a*self.moles**2)/self.volume**2)
        term2 = (self.volume - self.moles*self.b)
        return term1*term2 == self.moles * R * self.temperature