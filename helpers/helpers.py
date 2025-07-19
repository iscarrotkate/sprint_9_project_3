import random
import string
from pathlib import Path

def generate_password():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits

    upper_str = ''.join(random.choices(uppercase, k=3))
    lower_str = ''.join(random.choices(lowercase, k=3))
    digit_str = ''.join(random.choices(digits, k=3))

    password = list(upper_str + lower_str + digit_str)
    random.shuffle(password)

    return ''.join(password)


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_email():
    return f'{generate_random_string(10)}@testmail.com'


def get_project_root():
    current_dir = Path(__file__).parent

    while True:
        if (current_dir / 'tests').exists():
            return current_dir
        current_dir = current_dir.parent


def get_resource_path(relative_path):
    project_root = get_project_root()
    return str(project_root / relative_path)