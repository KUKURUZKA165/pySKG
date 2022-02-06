import random
import string


def generate_block():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))  # thanks stackoverflow


def generate_key():
    return generate_block() + "-" + generate_block() + "-" + generate_block()


def save(text):
    print(text)
    with open('generated_keys.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n{text}")
