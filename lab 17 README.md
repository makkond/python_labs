**Лабораторна робота №17: Використання Структур Даних та Алгоритмів у Python**

**Мета роботи**

Ознайомлення з основними структурами даних та алгоритмами у Python та їх застосування для вирішення практичних задач.

**Завдання:**
Task 1: Створити генератор number_generator(), який приймає список чисел і ітерує по ньому.

Task 2: Створити генератор even_number_generator(), який приймає початок та кінець діапазону і видає парні числа з цього діапазону.

Task 3: Створити генератор odd_number_generator(), який приймає початок та кінець діапазону і видає непарні числа з цього діапазону.

Task 4: Створити генератор fibonacci_generator(), який безкінечно видає числа Фібоначчі.

Task 5: Створити генератор prime_number_generator(), який приймає межу і видає прості числа до цієї межі.

Task 6: Створити генератор pre_order_traversal(), який приймає корінь бінарного дерева і видає елементи в префіксному порядку.

Task 7: Створити генератор in_order_traversal(), який приймає корінь бінарного дерева і видає елементи в інфіксному порядку.

Task 8: Створити генератор post_order_traversal(), який приймає корінь бінарного дерева і видає елементи в постфіксному порядку.

Task 9: Створити генератор dfs_traversal(), який приймає граф та стартову вершину і обходить граф за допомогою DFS.

Task 10: Створити генератор bfs_traversal(), який приймає граф та стартову вершину і обходить граф за допомогою BFS.

Task 11: Створити генератор dict_keys_generator(), який приймає словник і видає його ключі.

Task 12: Створити генератор dict_values_generator(), який приймає словник і видає його значення.

Task 13: Створити генератор dict_items_generator(), який приймає словник і видає його пари ключ-значення.

Task 14: Створити генератор file_lines_generator(), який приймає шлях до файлу і видає рядки з цього файлу один за одним.

Task 15: Створити генератор file_words_generator(), який приймає шлях до файлу і видає слова з цього файлу один за одним.

Task 16: Створити генератор string_chars_generator(), який приймає рядок і видає його символи один за одним.

Task 17: Створити генератор unique_elements_generator(), який приймає список і видає його унікальні елементи.

Task 18: Створити генератор reverse_list_generator(), який приймає список і видає його елементи у зворотному порядку.

Task 19: Створити генератор cartesian_product_generator(), який приймає два списки і видає їх декартовий добуток.

Task 20: Створити генератор permutations_generator(), який приймає список і видає його перестановки.

Task 21: Створити генератор combinations_generator(), який приймає список і видає його комбінації різної довжини.

Task 22: Створити генератор tuple_list_generator(), який приймає список кортежів і ітерує по ньому.

Task 23: Створити генератор parallel_lists_generator(), який приймає кілька списків і видає їх елементи паралельно.

Task 24: Створити генератор flatten_list_generator(), який приймає вкладений список і видає його елементи.

Task 25: Створити генератор nested_dict_generator(), який приймає вкладений словник і видає його ключі та значення.

Task 26: Створити генератор powers_of_two_generator(), який приймає число n і видає степені 2 до цього числа.

Task 27: Створити генератор powers_of_base_generator(), який приймає основу і межу, і видає степені цієї основи до межі.

Task 28: Створити генератор squares_generator(), який приймає початок та кінець діапазону і видає квадрати чисел з цього діапазону.

Task 29: Створити генератор cubes_generator(), який приймає початок та кінець діапазону і видає куби чисел з цього діапазону.

Task 30: Створити генератор factorials_generator(), який приймає межу і видає факторіали чисел до цієї межі.

Task 31: Створити генератор collatz_sequence_generator(), який приймає число і видає послідовність Коллатца для цього числа.

Task 32: Створити генератор geometric_progression_generator(), який приймає початковий член, знаменник та межу і видає числа у геометричній прогресії до цієї межі.

Task 33: Створити генератор arithmetic_progression_generator(), який приймає початковий член, різницю та межу і видає числа в арифметичній прогресії до цієї межі.

Task 34: Створити генератор running_sum_generator(), який приймає список чисел і видає їх накопичувальну суму.

Task 35: Створити генератор running_product_generator(), який приймає список чисел і видає їх накопичувальний добуток.


**Приклади використання функцій:**

Task 1: Генератор для ітерації по списку чисел
```python
def number_generator(numbers):
    for number in numbers:
        yield number
```

Task 2: Генератор, який видає парні числа в заданому діапазоні
```python
def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number
```

Task 3: Генератор, який видає непарні числа в заданому діапазоні
```python
def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number
```

Task 4: Генератор, який видає числа Фібоначчі безкінечно
```python
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
```

Task 5: Генератор, який видає прості числа до заданої межі
```python
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
```

Task 6: Генератор для обходу бінарного дерева в префіксному порядку
```python
def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)
```

Task 7: Генератор для обходу бінарного дерева в інфіксному порядку
```python
def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)
```

Task 8: Генератор для обходу бінарного дерева в постфіксному порядку
```python
def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value
```

Task 9: Генератор для обходу графу за допомогою DFS
```python
def dfs_traversal(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))
```

Task 10: Генератор для обходу графу за допомогою BFS
```python
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
```

Task 11: Генератор, який видає ключі словника
```python
def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key
```

Task 12: Генератор, який видає значення словника
```python
def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value
```

Task 13: Генератор для ітерації по парам ключ-значення словника
```python
def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item
```

Task 14: Генератор, який видає рядки з файлу один за одним
```python
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()
```

Task 15: Генератор для ітерації по словам у текстовому файлі
```python
def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word
```

Task 16: Генератор, який видає символи з рядка один за одним
```python
def string_chars_generator(string):
    for char in string:
        yield char
```

Task 17: Генератор, який видає унікальні елементи зі списку
```python
def unique_elements_generator(elements):
    seen = set()
    for element in elements:
        if element not in seen:
            yield element
            seen.add(element)
```

Task 18: Генератор, який видає елементи списку у зворотному порядку
```python
def reverse_list_generator(elements):
    for element in reversed(elements):
        yield element
```

Task 19: Генератор для декартового добутку двох списків
```python
def cartesian_product_generator(list1, list2):
    for product in itertools.product(list1, list2):
        yield product
```

Task 20: Генератор, який видає перестановки списку
```python
def permutations_generator(elements):
    for permutation in itertools.permutations(elements):
        yield permutation
```

Task 21: Генератор, який видає комбінації елементів списку
```python
def combinations_generator(elements):
    for length in range(1, len(elements) + 1):
        for combination in itertools.combinations(elements, length):
            yield combination
```

Task 22: Генератор для ітерації по списку кортежів
```python
def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup
```

Task 23: Генератор, який видає елементи з декількох списків паралельно
```python
def parallel_lists_generator(*lists):
    for values in zip(*lists):
        yield values
```

Task 24: Генератор, який видає елементи з вкладеного списку
```python
def flatten_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list_generator(element)
        else:
            yield element
```

Task 25: Генератор, який видає елементи з вкладеного словника
```python
def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)
```

Task 26: Генератор, який видає степені 2 до заданого числа
```python
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i
```

Task 27: Генератор, який видає степені заданої основи до вказаної межі
```python
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base
```

Task 28: Генератор, який видає квадрати чисел у заданому діапазоні
```python
def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2
```

Task 29: Генератор, який видає куби чисел у заданому діапазоні
```python
def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3
```

Task 30: Генератор, який видає факторіали чисел до заданої межі
```python
def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)
```

Task 31: Генератор, який видає числа у послідовності Коллатца
```python
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1  # Finally yield 1 as per the sequence rule
```

Task 32: Генератор, який видає числа у геометричній прогресії
```python
def geometric_progression_generator(a, r, limit):
    term = a
    while term <= limit:
        yield term
        term *= r
```

Task 33: Генератор, який видає числа в арифметичній прогресії
```python
def arithmetic_progression_generator(a, d, limit):
    term = a
    while term <= limit:
        yield term
        term += d
```

Task 34: Генератор, який видає накопичувальну суму списку чисел
```python
def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total
```

Task 35: Генератор, який видає накопичувальний добуток списку чисел
```python
def running_product_generator(numbers):
    total = 1
    for number in numbers:
        total *= number
        yield total
```

Інструкції з запуску:

-Вимоги до середовища: Python 3.x -Необхідні бібліотеки: всі необхідні бібліотеки є стандартними для Python 3.x -Для запуску програми потрібно завантажити файл student_main(17).py 
та виконати його з командного рядка або будь-якого інтегрованого середовища розробки (IDE), наприклад, PyCharm або VSCode.

**Висновки:**

Лабораторна робота   демонструє моє розуміння різноманітних структур даних та алгоритмів через використання генераторів. 
Кожен завдання відобразило мою здатність ефективно працювати з числами,
текстом, бінарними деревами, графами та іншими складними структурами даних.
