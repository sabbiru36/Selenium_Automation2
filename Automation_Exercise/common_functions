import string
import random


def random_email():
    domain = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    letters = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(letters) for _ in range(5))
    domain_name = random.choice(domain)
    email = f"{username}@{domain_name}"
    return email


def random_string():
    letters = string.ascii_lowercase + string.digits
    random_name = ''.join(random.choice(letters) for _ in range(8))
    string_random = f"{random_name}"
    return random_name


def random_number():
    numbers = string.digits
    random_numbers = ''.join(random.choice(numbers) for _ in range(8))
    string_random = f"{random_numbers}"
    return numbers


def store_user_data(filename, data_list):
    existing_data = []
    try:
        with open(filename, 'r') as file:
            existing_data = file.readlines()
    except FileNotFoundError:
        pass

    data_set = set(data_list)
    # append the set as new line
    with open(filename, 'a') as file:
        file.write(' '.join(data_set) + '\n')
