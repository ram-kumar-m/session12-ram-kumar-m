from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.log(X)
@print_log
def log(x):
    """ Natural logarythm of x """
    return func.evalf(subs={X: x})
@print_log
def dlog(x):
    """ Derivative of Natural logarythm of x """
    return sympy.diff(func, X).evalf(subs={X: x})