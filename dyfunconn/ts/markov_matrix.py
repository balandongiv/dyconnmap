""" Markov matrix


"""
import numpy as np


def markov_matrix(symts):
    """ Markov Matrix


    Parameters
    ----------
    symts :
        Discrete time series


    Returns
    -------
    mtx : matrix
        The

    """

    symbols = np.unique(symts)
    l = len(symbols)

    mtx = np.zeros((l, l))

    for i in range(len(symts) - 1):
        curr = symts[i]
        next = symts[i+1]

        mtx[curr, next] += 1

    mtx /= float(len(symts))

    return mtx
