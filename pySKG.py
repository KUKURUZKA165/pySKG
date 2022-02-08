from gen import *
from asyncio import run


async def main():
    print(r"              ____  _  ______ ")
    print(r"  _ __  _   _/ ___|| |/ / ___|")
    print(r" | '_ \| | | \___ \| ' / |  _ ")
    print(r" | |_) | |_| |___) | . \ |_| |")
    print(r" | .__/ \__, |____/|_|\_\____|")
    print(r" |_|    |___/                 ")
    user_input = int(input("1 - Save keys to file\n"
                           "2 - Generate and activate in steam client\n"
                           "Choose: "))
    if user_input == 1:
        await menu_1()
    elif user_input == 2:
        await menu_2()
    else:
        print("Error. What did you mean?")


if __name__ == "__main__":
    run(main())
