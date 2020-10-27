from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.tan(X)
@print_log
def tan(x):
    """ Tangent of x """
    return func.evalf(subs={X: x})
@print_log
def dtan(x):
    """Derivative of tangent of x"""
    return sympy.diff(func, X).evalf(subs={X: x})