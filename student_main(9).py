import re

def task1(letter_digit):
    return bool(re.match(r"^[a-z0-9]*[a-z][a-z0-9]*[0-9][a-z0-9]*$", letter_digit))

def task2(upper_letter):
    return bool(re.search(r"[A-Z]", upper_letter))

def task3(ip_address):
    return bool(re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", ip_address))

def task4(time):
    return bool(re.match(r"^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", time))

def task5(postal_code):
    return bool(re.search(r".*(\d{5}(\-\d{4})?)$", postal_code))

def task6(username):
    return bool(re.search(r"^[a-z0-9_-]{6,12}$", username))

def task7(credit_card):
    return bool(re.match(r"^(4|5|6)\d{3}-?\d{4}-?\d{4}-?\d{4}$", credit_card))

def task8(security_number):
    return bool(re.match(r"^\d{3}-\d{2}-\d{4}$", security_number))

def task9(valid_password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$', valid_password))

def task10(valid_ip):
    return bool(re.match(r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$', valid_ip))
