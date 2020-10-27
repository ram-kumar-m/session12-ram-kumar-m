from .printdec import print_log
@print_log
def relu(x):
    """ Returns ReLU Out for the given input """
    return x if x > 0 else 0
@print_log
def drelu(x):
    """ Returns derivative of relu of given x """
    if x == 0:
        return "Not Defined at 0"
    else:
        return 0 if x < 0 else 1 
