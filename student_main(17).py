import itertools
import math
# Task 1: Generator to iterate over a list of numbers
def number_generator(numbers):
    for number in numbers:
        yield number

# Task 2: Generator that yields even numbers from a given range
def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

# Task 3: Generator to yield odd numbers within a specified range
def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

# Task 4: Generator that produces Fibonacci numbers indefinitely
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5: Generator that yields prime numbers up to a given limit
def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number

# Task 6: Generator to traverse a binary tree in pre-order
def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

# Task 7: Generator for in-order traversal of a binary tree
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

# Task 8: Generator for post-order traversal of a binary tree
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

# Task 9: Generator to traverse a graph using DFS
def dfs_traversal(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

# Task 10: Generator for BFS traversal of a graph
def bfs_traversal(graph, start):
    from collections import deque
    queue = deque([start])
    visited = set()
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            queue.extend(graph[vertex])

# Task 11: Generator that yields the keys of a dictionary
def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key

# Task 12: Generator that yields the values of a dictionary
def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

# Task 13: Generator to iterate over key-value pairs of a dictionary
def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

# Task 14: Generator that yields lines from a file one by one
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 15: Generator to iterate over words in a text file
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16: Generator that yields characters from a string one by one
def string_chars_generator(string):
    for char in string:
        yield char

# Task 17: Generator to yield unique elements from a list
def unique_elements_generator(elements):
    seen = set()
    for element in elements:
        if element not in seen:
            yield element
            seen.add(element)

# Task 18: Generator that yields elements of a list in reverse order
def reverse_list_generator(elements):
    for element in reversed(elements):
        yield element

# Task 19: Generator for Cartesian product of two lists
def cartesian_product_generator(list1, list2):
    for product in itertools.product(list1, list2):
        yield product

# Task 20: Generator that yields permutations of a list
def permutations_generator(elements):
    for permutation in itertools.permutations(elements):
        yield permutation

# Task 21: Generator that yields combinations of a list of elements
def combinations_generator(elements):
    for length in range(1, len(elements) + 1):
        for combination in itertools.combinations(elements, length):
            yield combination

# Task 22: Generator to iterate over a list of tuples
def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup

# Task 23: Generator that yields elements from multiple lists in parallel
def parallel_lists_generator(*lists):
    for values in zip(*lists):
        yield values

# Task 24: Generator that yields elements from a nested list
def flatten_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list_generator(element)
        else:
            yield element

# Task 25: Generator to yield elements from a nested dictionary
def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

# Task 26: Generator to yield powers of 2 up to a given number
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

# Task 27: Generator that yields powers of a given base up to a specified limit
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Task 28: Generator to yield the squares of numbers in a given range
def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2

# Task 29: Generator to yield cubes of numbers in a specified range
def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3

# Task 30: Generator that yields factorials of numbers up to a given limit
def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)

# Task 31: Generator to yield numbers in the Collatz sequence
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1  # Finally yield 1 as per the sequence rule

# Task 32: Generator that yields numbers in a geometric progression
def geometric_progression_generator(a, r, limit):
    term = a
    while term <= limit:
        yield term
        term *= r

# Task 33: Generator to yield numbers in an arithmetic progression
def arithmetic_progression_generator(a, d, limit):
    term = a
    while term <= limit:
        yield term
        term += d

# Task 34: Generator that yields the running sum of a list of numbers
def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

# Task 35: Generator to yield the running product of a list of numbers
def running_product_generator(numbers):
    total = 1
    for number in numbers:
        total *= number
        yield total
