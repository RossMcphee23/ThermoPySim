from .base_engine import HeatEngine

class CarnotEngine(HeatEngine):
    def efficiency(self):
        return 1 - (self.cold_temp / self.hot_temp)
