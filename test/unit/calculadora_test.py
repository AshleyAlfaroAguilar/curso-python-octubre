#PYTHONPATH ="C:\Users\Lenovo\code\CursoPyhtonOctubre"
#import os, sys 
#sys.path =os.environ["PYTHONPATH"]
#probar otro dia 

from calculadora import sumar, restar

# Happy Path
def test_sumar_function_add_two_numbers():
    result =sumar(3,5)

    assert result ==8

def test_restar_function_substract_two_numbers():
    result = restar(9,3)

    assert result == 6

# Edge cases
def test_sumar_function_fails_if_first_number_receives_letters():
    result = sumar ('a', 5)

    assert result == 'error esto no es un numero'
