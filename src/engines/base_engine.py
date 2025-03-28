class HeatEngine:
    def __init__(self, hot_temp, cold_temp):
        self.hot_temp = hot_temp
        self.cold_temp = cold_temp

    def efficiency(self):
        raise NotImplementedError("Derived classes must implement this method.")
