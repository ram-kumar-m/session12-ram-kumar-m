# Assignment 12
## Build a calculator package that has separate module for:
1. sin, cos, tan, tanh, SoftMax, Sigmoid, ReLU, log and e
2. The modules shall include their derivatives as well
1. If we do import calculator, we should be able to access all the above function (except deviratives)
1. For derivates we must do: from package import derivatives. 
1. Outputs are returned as well as printed using only f-string
1. Write simple test cases to check the outputs of each operator and their derivative


# __Simple Calulus functions in Python__
This module constains functions sin, cos, e (exponential funtion), log, relu, sigmoid, softmax, tan, tanh and their corresponding derivatives dsin, dcos, de, dlog, drelu, dsigmoid, dsoftmax, dtan, dtanh respectively 
written in python using sympy and math.

## Invocation:
To import the main functions without the derivates.
`import calulator` or `from calculator import *`

to import the derivative functions
`import derivatives from calculator`


## __Modules__
> Saves in  a directory called `ouput` in current working directory if no output path is specified.

  ##  `sin`
    Computes the sin or its derivative, (radian input) 
  
 ## `cos`
    Computes the sin or its derivative, (radian input)
  ##  `tan`
    Computes the tangent or its derivative, (radian input) 
  
 ## `tanh`
    Computes the hyperbolic tangent or its derivative, (radian input)
 
 ## `e`
    Computes the exponential at that point (e to the power x) or its derivative
 
 ## `log`
    Computes the natural logarythm at that point (ln x) or its derivative

 ## `relu`
    Computes the ReLU(Rectified Linear Unit) function at that point or its derivative

 ## `sigmoid`
    Computes the Sigmoid function at that point or its derivative

 ## `softmax`
    Computes the Soft function for a given set of inputs.
    or its corresponding derivative.
   > Multiple Inputs Required.



## **Test Cases (Pytest)**
>The names of the tests are so that `'test_'` prefix is added to the function it tests, suffied by the what the test does.

### `test_readme_exists`
   Checks if there is a README.md file in the same folder.

### `test_readme_contents`
   Checks if the README.md file has alteast 500 words.

### `test_readme_proper_description`
   Checks if the required functions are present in the README.md file.

### `test_readme_file_for_formatting`
   Checks if there are adequete headings present in the README.md file.

### `test_indentations`
   Checks if proper indentations are present throughout the python file.
   using the rule of 4 spaces equals 1 Tab.

### `test_function_name_had_cap_letter`
   Checks if any one the functions have capital letters used in their names, which breaks the PEP8 conventions.
   
### _Annotation and Docstring tests_
tests if any of the functions in function list don't have annotations or docstrings

### `test_sin`
 Check sin function

### `test_cos`
 Check cos function

### `test_tan`
 Check tan function

### `test_tanh`
 Check tanh function

### `test_relu`
 Check ReLU function

### `test_log`
 Check log function

### `test_e`
 Check exp function

### `test_sigmoid`
 Check sigmoid function

### `test_softmax`
 Check your softmax function

### `test_softmax_min_args`
 Check for multiple arguments for softmax input

### `test_dsin`
 Check derivative of sin function

### `test_dcos`
 Check derivative of cos function

### `test_dtan`
 Check derivative of tan function

### `test_dtanh`
 Check derivative of tanh function

### `test_drelu`
 Check derivative of ReLU function

### `test_dlog`
 Check derivative of log function

### `test_de`
 Check derivative of exponential function

### `test_dsigmoid`
 Check derivative of sigmoid function

### `test_dsoftmax`
 Check derivative of softmax inputs

