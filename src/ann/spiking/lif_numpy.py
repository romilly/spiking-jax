"""
Simulate an array of refactory leaky integrate and fire neurons for a single time period
"""


# parameters
from ann.spiking.parameters import *


import numpy as np


def initial_state(count):
    potentials = np.full(count, initial_potential)
    ts = np.zeros(count)
    injected_currents = na * (np.array(range(count)) + 1)
    return injected_currents, potentials, ts


def step(v, tr, injected_current):
    rv = np.full_like(v, reset_voltage)
    dv = ((resting_potential - v) + (injected_current * membrane_resistance)) * (dt / tau_m)
    spikes = v > threshold
    next_v = np.where(spikes, rv, v + dv)
    refactory = tr > 0
    next_v = np.where(refactory, rv, next_v)
    next_tr = np.where(refactory, tr - 1, tr)
    R_DUR = int(refactory_period / dt)
    next_tr = np.where(spikes, R_DUR, next_tr)
    return next_v, next_tr, spikes
