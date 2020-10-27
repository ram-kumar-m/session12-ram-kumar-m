from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.sin(X)
@print_log
def sin(x):
    """ Sine of x """
    return func.evalf(subs={X: x})
@print_log
def dsin(x):
    """Derivative of Sine of x """
    return sympy.diff(func, X).evalf(subs={X: x})
