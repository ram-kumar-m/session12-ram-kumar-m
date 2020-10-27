
import pytest
import random
import os
import inspect
import re
import subprocess
from pathlib import Path
import os
import shutil
import math
import calculator as calc
from calculator import derivatives as D

README_CONTENT_CHECK_FOR = []

CHECK_FOR_THINGS_NOT_ALLOWED = []

# def test_for_docstrings():
#     for func in main_funcs:
#         assert func[1].__doc__ , f'Function {func[0]} has no doc string'

# def test_for_annotations():
#     for func in main_funcs:
#         assert func[1].__annotations__ , f'Function {func[0]} has no annotations'

def test_sin():
    assert math.sin(3.14) == calc.sin(3.14), 'Check sin function'

def test_cos():
    assert math.cos(3.14) == calc.cos(3.14), 'Check cos function'

def test_tan():
    assert math.tan(3.14) == calc.tan(3.14), 'Check tan function'

def test_tanh():
    assert math.tanh(3.14) == calc.tanh(3.14), 'Check tanh function'

def test_relu():
    assert 3.14 == calc.relu(3.14), 'Check ReLU function'

def test_log():
    assert math.log(3) == calc.log(3), 'Check log function'

def test_e():
    assert math.exp(3) == calc.e(3), 'Check exp function'

def test_sigmoid():
    assert calc.sigmoid(0) == 0.5, 'Check sigmoid function'

def test_softmax():
    out = (0.09003057317038046, 0.24472847105479767, 0.6652409557748219)
    exp_out = calc.softmax(1, 2, 3)
    for i, j in zip(out, exp_out):
        assert math.isclose(i, j), 'Check your softmax function'
        
def test_softmax_min_args():
    with pytest.raises(ValueError):
        calc.softmax(1)


def test_dsin():
    assert math.cos(3.14/2) == D.dsin(3.14/2), 'Check derivative of sin function'

def test_dcos():
    assert -1*math.sin(3.14/4) == D.dcos(3.14/4), 'Check derivative of cos function'

def test_dtan():
    assert math.cos(3.14/4)**-2 == D.dtan(3.14/4), 'Check derivative of tan function'

def test_dtanh():
    assert math.cosh(3.14/4)**-2 == D.dtanh(3.14/4), 'Check derivative of tanh function'

def test_drelu():
    assert 1 == D.drelu(3.14), 'Check derivative of relu function'

def test_dlog():
    assert 1/3 == D.dlog(3), 'Check derivative of log function'

def test_de():
    assert math.exp(3) == D.de(3), 'Check derivative of exp function'

def test_dsigmoid():
    assert D.dsigmoid(0) == 0.25, 'Check derivative of sigmoid function'

def test_dsoftmax():
    exp_out = [0.08192506906499324, 0.18483644650997874, 0.22269542653462335]
    out = D.dsoftmax(1, 2, 3)
    for i, j in zip(out, exp_out):
        assert math.isclose(i, j), 'Check derivative of sigmoid function'




def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(
        readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(main)
#     spaces = re.findall('\n +.', lines)
#     for count, space in enumerate(spaces):
#         assert len(space) % 4 == 2, f"Your script contains misplaced indentations at \
# n'th postion {count+1} starting \n with {space}"
#         assert len(re.sub(
#             r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


# def test_function_name_had_cap_letter():
#     functions = inspect.getmembers(main, inspect.isfunction)
#     for function in functions:
#         assert len(re.findall(
#             '([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

