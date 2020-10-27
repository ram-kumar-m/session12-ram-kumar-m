import math
from .printdec import print_log
@print_log
def sigmoid(x):
    """ Sigmoid of x """
    return 1/(1+math.exp(-x))
@print_log
def dsigmoid(x):
    """Derivative of Sigmoid of x """
    return sigmoid(x) * (1 - sigmoid(x))