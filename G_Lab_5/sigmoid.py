import numpy as np
from scipy.special import expit

def sigmoid(z):
	# TODO: вычислить значение g(z) по формуле из методических указаний
	# g_z =
    g_z = np.zeros(z.shape)
    g_z=expit(z)
    return g_z

