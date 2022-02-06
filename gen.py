import time
from utils import *


def menu_1():
    howmany = int(input("\nHow many keys do you want to generate?\nInput: "))
    start_time = time.time()
    result = ""
    count = 0
    if howmany >= 20000:
        print("Generating. Please Wait.")
    else:
        print(f"OK, Saving {howmany} key(s) to generated_keys.txt:")

    while count < howmany:
        result += generate_key() + "\n"
        count = count + 1
    save(f"\nGenerated at {time.ctime()}")
    save(result)

    donefor = round(time.time() - start_time, 2)
    if donefor >= 0.01:
        save(f"Done for {round(time.time() - start_time, 2)} seconds")
    else:
        save("Done!")


def menu_2():
    print("Placeholder! Activating generated keys inside steam is not implemented yet.")
