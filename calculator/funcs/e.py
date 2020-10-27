from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.exp(X)

@print_log
def e(x):
    """ Exponential of x """
    return func.evalf(subs={X: x})
@print_log
def de(x):
    """ Derivative of Exponential of x """
    return sympy.diff(func, X).evalf(subs={X: x})