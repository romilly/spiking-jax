"""
Simulate a refactory leaky integrate and fire neuron for a single time period
"""


# parameters
from ann.spiking.parameters import *


def step(v, tr, injected_current):
    spiking = False
    if tr > 0:
        next_v = reset_voltage
        tr = tr - 1
    elif v > threshold:
        next_v = reset_voltage
        tr = int(refactory_period / dt)
        spiking = True
    else:
        dv = ((resting_potential - v) + (injected_current * membrane_resistance)) * (dt / tau_m)
        next_v = v + dv
    return next_v, tr, spiking