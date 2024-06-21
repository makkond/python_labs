**Лабораторна робота №15: Overview of Big Data Technologies**

**Мета роботи:**
Ознайомлення з основними технологіями обробки великих даних та їх застосування в Python.

**Завдання:**

Task 1: Clean Data
Створити функцію clean_data(), яка приймає довгий рядок даних, розділених комами, і використовує map() для повернення списку даних, кожен з яких позбавлений пробілів і переведений в нижній регістр.

Task 2: Filter Emails
Створити функцію filter_emails(), яка приймає довгий рядок, що містить адреси електронної пошти, і використовує filter() для повернення списку лише дійсних адрес електронної пошти. Адреса є дійсною, якщо вона містить рівно один символ '@'.

Task 3: Extract Keywords
Створити функцію extract_keywords(), яка приймає довгий рядок слів і використовує filter() для повернення списку слів, які довші за вказану довжину.

Task 4: Process Text Data
Створити функцію process_text(), яка приймає довгий рядок текстових даних і використовує map() для видалення пробілів, спеціальних символів і переведення тексту в нижній регістр, а потім використовує filter() для повернення списку без порожніх або дуже коротких записів.

Task 5: Normalize Data
Створити функцію normalize_data(), яка приймає довгий рядок числових значень, розділених комами, і нормалізує їх до діапазону від 0 до 1 на основі максимального значення.

Task 6: Concatenate Strings
Створити функцію concatenate_strings(), яка приймає кілька рядків, розділених спеціальним символом, і конкатенує їх в один рядок без цього роздільника.

Task 7: Sum Numeric Strings
Створити функцію sum_numeric_strings(), яка приймає рядок, що містить числа, розділені комами, і обчислює їх суму.

Task 8: Filter Numbers
Створити функцію filter_numbers(), яка використовується для фільтрації чисел з рядка, значення яких вище заданого порогу.

Task 9: Map to Squares
Створити функцію map_to_squares(), яка приймає рядок чисел, конвертує їх у їх квадрати і повертає список цих значень.

Task 10: Reverse Strings
Створити функцію reverse_strings(), яка приймає рядок слів, розділених комами, і реверсує кожне слово.


**Приклади використання функцій:**

1) Clean Data
```python
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)
print(cleaned_data)  # Output: ['apple', 'banana', 'orange']
```
Ця функція очищує рядок від пробілів і перетворює кожен елемент у нижній регістр.

2) Filter Emails
```python
emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails)  # Output: ['test@example.com', 'example@test.co']
```
Ця функція фільтрує із вхідного рядка лише дійсні електронні адреси.

3) Extract Keywords
```python
words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words)  # Output: ['apple', 'banana']
```
Ця функція витягує з рядка слова, довжина яких більша за задану.

4)Process Text Data
```python
texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts)  # Output: ['hello', 'yes', 'no']
```
Ця функція обробляє текст, видаляючи спеціальні символи і приводячи до нижнього регістру.

5)Normalize Data
```python
numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers)  # Output: [0.2, 0.4, 0.6, 0.8, 1.0]
```
Ця функція нормалізує числові значення до діапазону від 0 до 1 на основі максимального значення.

6)Concatenate Strings
```python
data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)
print(concatenated_data)  # Output: "Hello World! How are you?"
```
Ця функція конкатенує рядки, розділені роздільником, в один рядок без цього роздільника.

7) Sum Numeric Strings
```python
numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)
print(sum_of_numeric_strings)  # Output: 100
```
Ця функція обчислює суму чисел, витягнутих з рядка.

8) Filter Numbers
```python
numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)
print(filtered_numbers)  # Output: [30, 40]
```
Ця функція фільтрує числа з рядка, залишаючи тільки ті, що більші за заданий поріг.

9)Map to Squares
```python
numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
```
Ця функція перетворює числа у рядку на їх квадрати.

10)Reverse Strings
```python
strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
print(reversed_strings)  # Output: ['elppa', 'ananab', 'egnaro', 'RAEP', 'iwik']
```
Ця функція реверсує кожне слово в рядку слів, розділених комами.

**Інструкції з запуску:** 

-Вимоги до середовища: Python 3.x -Необхідні бібліотеки: всі необхідні бібліотеки є стандартними для Python 3.x -Для запуску програми потрібно завантажити файл student_main(15).py 
та виконати його з командного рядка або будь-якого інтегрованого середовища розробки (IDE), наприклад, PyCharm або VSCode.

**Висновки**

У цій лабораторній роботі було розглянуто імплементацію функцій для роботи зі строками даних, електронними адресами, числовими значеннями, словами та текстом.
Кожна функція була реалізована з використанням вбудованих методів Python,таких як map(), filter(), split(), join() та регулярних виразів для досягнення потрібного функціоналу.
