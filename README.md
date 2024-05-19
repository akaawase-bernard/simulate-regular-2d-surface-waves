# Simulate-regular-2d-surface-waves


This repository contains a Python script for generating and animating ocean surface waves. The script simulates both long and short waves propagating over a spatial grid, and includes functionality to track and visualize wave height at a specific buoy location.

## Features

- **Wave Generation**: Simulates ocean waves using a combination of a main wave and several short waves.
- **Wave Propagation**: Animates the propagation of waves over time.
- **Visualization**: Generates frames showing the wave field and the wave height time series side by side.

## Parameters

- `length`: Length of the spatial grid (default: 150).
- `width`: Width of the spatial grid (default: 150).
- `main_amplitude`: Amplitude of the main wave (default: 2.1).
- `main_wavelength`: Wavelength of the main wave (default: 20).
- `main_direction`: Direction of the main wave propagation in radians (default: π/4).
- `num_short_waves`: Number of short waves (default: 5).
- `short_amplitude`: Amplitude of the short waves (default: 0.11).
- `num_frames`: Number of frames for the animation (default: 1000).
- `time_step`: Time interval between frames (default: 0.2).

## Usage

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/akaawase-bernard/simulate-regular-2d-surface-waves.git
    cd simulate-regular-2d-surface-waves
    ```

2. **Install Dependencies**:
    Make sure you have `numpy` and `matplotlib` installed. You can install them using pip:
    ```bash
    pip install numpy matplotlib
    ```

3. **Run the Script**:
    ```bash
    python wave_simulation.py
    ```

This will generate and save frames of the wave animation in the `wave_frames` directory.


## Acknowledgments

This project was created by Akaawase Bernard in 2024.
