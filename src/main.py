from utilities.plot_utils import plot_isothermal_process

def main():
    initial_volume = 1  # m3
    final_volume = 5    # m3
    pressure = 101325   # Pa (not used for isothermal plot here)
    n_moles = 1         # mol
    temperature = 300   # K

    print("plotting the iso process..")
    plot_isothermal_process(initial_volume, final_volume, pressure, n_moles, temperature)

if __name__ == "__main__":
    main()