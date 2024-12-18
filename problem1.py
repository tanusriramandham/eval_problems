""" 1)  Write a Python program that accepts a string containing a mathematical expression and a dictionary of variables. The program should evaluate the expression only using the variables in the dictionary.
 expression = "a + b * c"
 variables = {"a": 4, "b": 2, "c": 3}
 output= 10
"""
def eval_expression(expression,vaiables):
    return eval(expression,{},variables)
expression="a+b*c"
variables={"a":4,'b':2,"c":3}
result=eval_expression(expression,variables)
print(result)