mv = 0.001
ms = 0.001
mmo = 0.001
na = 1E-9
megohm = 1E6

# typical neuron parameters
threshold = -50 * mv     # spike threshold [mV]
reset_voltage = -65 * mv  # reset potential [mV]
tau_m = 8. * ms     # membrane time constant [ms]
membrane_resistance = 10 * megohm    # membrane resistance [MOhm]
initial_potential = -75 * mv   # initial potential [mV]
resting_potential = -70 * mv      # resting potential [mV]
refactory_period = 3. * ms      # refractory time (ms)
I = 1.0 * na # base injection current [mA]

# simulation parameters
dt = 0.1 * ms  # Simulation time step [ms]
R_DUR = int(refactory_period / dt)