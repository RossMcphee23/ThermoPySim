class ThermodynamicSystem:
    def __init__(self, pressure, volume, temperature, moles):
        self.pressure = pressure
        self.volume = volume
        self.temperature = temperature
        self.moles = moles

    def update_state(self, pressure=None, volume=None, temperature=None):
        if pressure:
            self.pressure = pressure
        if volume:
            self.volume = volume
        if temperature:
            self.temperature = temperature

    def state_equation(self):
        raise NotImplementedError("Derived classes must implement this method.")
