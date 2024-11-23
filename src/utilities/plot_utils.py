import matplotlib.pyplot as plt

def plot_pv_diagram(volumes, pressures, title="PV Diagram"):
    plt.plot(volumes, pressures, marker='o')
    plt.title(title)
    plt.xlabel("Volume (m³)")
    plt.ylabel("Pressure (Pa)")
    plt.grid(True)
    plt.show()
