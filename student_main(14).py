def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a and not b) or (b and not a)

def greet(a=True, b=False):
    return "Hello world" if a else "Goodbye world"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(boolean_list):
    return sum(boolean_list)

def parity(num):
    binary = bin(num)[2:]
    ones = binary.count('1')
    if ones % 2 == 0:
        return True
    else:
        return False

def majority_vote(a, b, c):
    return (a + b + c) > 1

def switch(value):
    return not value

def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(boolean_list):
    return [value for value in boolean_list if value]

def multiplexer(a, b, c, int):
    if a:
        return int * 2
    elif b:
        return int * 3
    elif c:
        return int - 5
    else:
        return int
