import jax
import math


def gwn(key, amplitude, duration: float, tau_m, dt: float):
    """
    generate  Gaussian White Noise values

    :param key:
    :param amplitude:
    :param duration: in ms
    :param tau_m: time constant, in ms
    :param dt: time step, in ms
    :return: array of noise values
    """
    steps = math.ceil(duration / dt)
    return amplitude * jax.random.normal(key, [steps]) * (tau_m / dt)
