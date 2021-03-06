from random import choice
from string import ascii_uppercase, digits
sym_rng = ascii_uppercase + digits


async def generate_key():
    return ''.join(choice(sym_rng) for _ in range(5)) + "-" + ''.join(choice(sym_rng) for _ in range(5)) + "-" + ''.join(choice(sym_rng) for _ in range(5))
# thanks stackoverflow


async def save(text):
    print(text)
    with open('generated_keys.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n{text}")


async def potential_key(text):
    print(text)
    with open('potential_keys.txt', 'a', encoding="utf-8") as file:
        file.write(f"\n{text}")
