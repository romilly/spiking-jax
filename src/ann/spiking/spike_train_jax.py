"""
Generate spike trains for neural input
"""

import jax.numpy as np


def periodic_spikes(firing_periods, duration: int):
    """
    create boolean spikes from from firing rates

    :param firing_periods:  number of time steps between firings
    :param duration: train duration in time steps
    :return: boolean matrix showing when each neuron fires. row = time, column = neuron

    Outer product via  broadcasting courtesy of @jakevdp
    """

    return 0 ==   (1 + np.arange(duration))[:, None] % firing_periods

