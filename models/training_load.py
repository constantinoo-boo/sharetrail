import numpy as np


def compute_trimp(duration_min, avg_hr, hr_rest, hr_max):
    """
    Calcul TRIMP basé sur modèle Banister
    """
    delta_hr = (avg_hr - hr_rest) / (hr_max - hr_rest)

    b = 1.92  # coefficient homme
    trimp = duration_min * delta_hr * np.exp(b * delta_hr)

    return trimp
