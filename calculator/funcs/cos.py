from .printdec import print_log
import sympy
X = sympy.symbols('X')

func = sympy.cos(X)

@print_log
def cos(x):
    """ Cosine of x """
    return func.evalf(subs={X: x})
    
@print_log
def dcos(x):
    """ Derivative of cosine of x """
    return sympy.diff(func, X).evalf(subs={X: x})
    
