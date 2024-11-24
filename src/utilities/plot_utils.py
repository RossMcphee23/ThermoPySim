import matplotlib.pyplot as plt

def plot_pv_diagram(volumes, pressures, title="PV Diagram"):
    plt.plot(volumes, pressures, marker='o')
    plt.title(title)
    plt.xlabel("Volume (m³)")
    plt.ylabel("Pressure (Pa)")
    plt.grid(True)
    plt.show()

def plot_isothermal_process(initial_volume, final_volume, pressure, n_moles, temperature):
    R = 8.314
    volumes = [v for v in range(initial_volume, final_volume + 1)]
    pressures = [(n_moles * R * temperature) / v for v in volumes]
    plot_pv_diagram(volumes, pressures, title="Isothermal Process")