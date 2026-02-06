import pandas as pd


def exponential_moving_average(series, tau):
    return series.ewm(span=tau, adjust=False).mean()


def compute_ctl_atl(load_series):
    """
    load_series = pandas Series indexée par date
    """
    ctl = exponential_moving_average(load_series, 42)
    atl = exponential_moving_average(load_series, 7)

    tsb = ctl - atl

    return ctl, atl, tsb
