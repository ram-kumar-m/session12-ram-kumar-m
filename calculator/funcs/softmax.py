from .printdec import print_log
import numpy as np

@print_log
def softmax(*args):
    """Compute the softmax of vector x."""
    if len(args) <2:
        raise ValueError('Atleast two rumbers required')
    exps = np.exp(args)
    return exps / np.sum(exps)
@print_log
def dsoftmax(*args):
    """Compute derivative of Softmax"""
    x = softmax(*args) 
    return x*(1-x)

