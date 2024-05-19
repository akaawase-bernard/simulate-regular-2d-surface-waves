import numpy as np
import matplotlib.pyplot as plt
import os

def generate_wave_map(length=100, width=100, main_amplitude=1, main_wavelength=40,
                      main_direction=np.pi/4, num_short_waves=5, short_amplitude=0.2, time=0):
    """
    Generate a spatial map of ocean surface waves.

    Parameters:
    - length (float): Length of the spatial grid.
    - width (float): Width of the spatial grid.
    - main_amplitude (float): Amplitude of the main wave.
    - main_wavelength (float): Wavelength of the main wave.
    - main_direction (float): Direction of the main wave propagation in radians.
    - num_short_waves (int): Number of short waves.
    - short_amplitude (float): Amplitude of the short waves.
    - time (float): Current time for wave propagation.

    Returns:
    - np.ndarray: Combined wave elevation at each grid point.
    """
    # Generate spatial grid
    x = np.linspace(0, length, 100)
    y = np.linspace(0, width, 100)
    X, Y = np.meshgrid(x, y)

    # Generate spatial map of main wave elevation
    k_main = 2 * np.pi / main_wavelength  # Wavenumber for main wave
    omega_main = np.sqrt(9.81 * k_main)  # Angular frequency for deep water waves
    phase_main = k_main * (np.cos(main_direction) * X + np.sin(main_direction) * Y) - omega_main * time
    main_wave = main_amplitude * np.cos(phase_main)

    # Parameters for the short waves
    short_wavelengths = np.random.uniform(10, 20, num_short_waves)  # Random short wave wavelengths
    short_directions = np.random.uniform(0, np.pi, num_short_waves)  # Random short wave directions

    # Generate spatial map of short waves elevation
    eta_short = np.zeros_like(X)
    for i in range(num_short_waves):
        k_short = 2 * np.pi / short_wavelengths[i]  # Wavenumber for short wave
        omega_short = np.sqrt(9.81 * k_short)  # Angular frequency for deep water waves
        phase_short = k_short * (np.cos(short_directions[i]) * X + np.sin(short_directions[i]) * Y) - omega_short * time
        eta_short += short_amplitude * np.cos(phase_short)

    # Combine main wave and short waves
    eta = main_wave + eta_short

    return X, Y, eta

# Parameters
length = 150
width = 150
main_amplitude = 2.1
main_wavelength = 20
main_direction = np.pi / 4
num_short_waves = 5
short_amplitude = 0.11
num_frames = 1000
time_step = 0.2

# Create directory for storing frames
output_dir = 'wave_frames'
os.makedirs(output_dir, exist_ok=True)

# Generate and save frames
for frame in range(num_frames):
    time = frame * time_step
    X, Y, eta = generate_wave_map(length=length, width=width, main_amplitude=main_amplitude,
                                  main_wavelength=main_wavelength, main_direction=main_direction,
                                  num_short_waves=num_short_waves, short_amplitude=short_amplitude, time=time)
    
    # Plotting
    plt.figure(figsize=(12, 11))
    plt.pcolormesh(X, Y, eta, cmap='Blues_r', shading='auto', vmin = -2, vmax=2)
    #plt.contourf(eta, levels=9, cmap='Blues_r', vmin = -2., vmax =2.)

    plt.colorbar(label='Wave Height (m)')
    plt.title(f' Sciencestical 2:  Ocean Waves (t={time:.1f}s)', fontsize = 20)

    #plt.title(f'Quasi-regular Waves (t={time:.1f}s)')
    plt.xlabel('X (m)', fontsize = 20)
    plt.ylabel('Y (m)', fontsize = 20)
    
    # Save the frame
    plt.savefig(f'{output_dir}/frame_{frame:03d}.png')
    plt.close()

print(f"Frames saved in the directory '{output_dir}'.")
