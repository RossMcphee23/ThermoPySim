import matplotlib.pyplot as plt

def plot_isothermal_process(initial_volume, final_volume, pressure, n_moles, temperature, save_path=None):
    R = 8.314
    volumes = [v for v in range(initial_volume, final_volume + 1)]
    pressures = [(n_moles * R * temperature) / v for v in volumes]
    
    # Plot the graph
    plt.figure()
    plt.plot(volumes, pressures, marker='o')
    plt.title("Isothermal Process")
    plt.xlabel("Volume (m³)")
    plt.ylabel("Pressure (Pa)")
    plt.grid(True)
    
    # Save or show the plot
    if save_path:
        plt.savefig(save_path)  # Save the plot as an image file
        print(f"Graph saved at: {save_path}")
    else:
        plt.show()
