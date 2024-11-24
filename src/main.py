from utilities.plot_utils import plot_isothermal_process

def main():
    # Define parameters for the isothermal process
    initial_volume = 1  # m³
    final_volume = 5    # m³
    pressure = 101325   # Pa (not used for isothermal plot here)
    n_moles = 1         # mol
    temperature = 300   # K

    # Save path for the graph
    save_path = "examples/isothermal_process.png"
    
    # Plot and save the isothermal process graph
    print("Plotting and saving the isothermal process graph...")
    plot_isothermal_process(initial_volume, final_volume, pressure, n_moles, temperature, save_path)

if __name__ == "__main__":
    main()
