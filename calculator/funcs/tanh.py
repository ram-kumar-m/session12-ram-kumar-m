from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.tanh(X)
@print_log
def tanh(x):
    """ Hyperbolic tangent of x """
    return func.evalf(subs={X: x})
@print_log
def dtanh(x):
    """Derivative of Hyperbolic tangent of x """
    return sympy.diff(func, X).evalf(subs={X: x})