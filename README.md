
# Traffic Generation Using 2-State MMPP

This project implements a Python program that generates traffic consisting of unit-size packets based on a 2-state Markov Modulated Poisson Process (MMPP), specifically an ON-OFF process. The program calculates parameters to generate traffic with the required average rate (`r`) and burst size (`B`).

## Features

- **Traffic Generation**: Generates traffic based on the specified average rate (`r`) and burst size (`B`).
- **Queue Simulation**: Simulates the buffer occupancy of a queue with the MMPP-generated traffic as the arrival process.
- **Visualization**: Generates plots to visualize the queue's occupancy over time.
- **Parameter Analysis**: Calculates the overall event rate and average burst size, verifying the correctness of the generated traffic against target parameters.

## Code Structure

### Main Functionality

- **`runMMPP(B, r)`**:
  - Simulates an ON-OFF MMPP traffic process.
  - Takes as input:
    - `B`: Average burst size (in packets).
    - `r`: Average traffic rate (packets per unit time).
  - Outputs:
    - Overall event rate.
    - Average burst size.
    - A plot showing queue occupancy over time.

### Example Scenarios

The program generates two traffic sequences with the following parameters:

1. **Sequence S1**: 
   - Average rate (`r`): 1 packet/unit time.
   - Average burst size (`B`): 20 packets.
2. **Sequence S2**: 
   - Average rate (`r`): 1.5 packets/unit time.
   - Average burst size (`B`): 3 packets.

## Results and Analysis

### Buffer Occupancy Plots

The program produces plots of buffer occupancy with the following configuration:
- A queue with a service rate of 1 packet per time slot.
- Simulation duration (`T`): 500 time slots.
- Each plot shows the maximum average queue occupancy in non-overlapping intervals of 5 time slots (100 ticks).

### Differences in Results

- **Sequence S1**:
  - Higher burst size leads to longer periods of high occupancy.
- **Sequence S2**:
  - Lower burst size results in more frequent, shorter bursts.

These differences are reflected in the buffer occupancy plots, illustrating how burst size affects queue dynamics.

## How to Run

1. Install required dependencies:
   ```bash
   pip install numpy matplotlib
   ```
2. Run the script:
   ```bash
   python Question4.py
   ```

## Dependencies

- Python 3.9 or higher
- NumPy
- Matplotlib

## Acknowledgments

This project was developed to explore traffic modeling using Markov processes and analyze its impact on queue performance.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

