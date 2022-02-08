from steam_tools import *
from time import sleep, ctime, time


async def menu_1():
    howmany = int(input("\nHow many keys do you want to generate?\nInput: "))
    start_time = time()
    result = ""
    count = 0
    if howmany >= 20000:
        print("Generating. Please Wait.")
    else:
        print(f"OK, Saving {howmany} key(s) to generated_keys.txt:")

    while count < howmany:
        result += ''.join(choice(sym_rng) for _ in range(5)) + "-" + ''.join(choice(sym_rng) for _ in range(5)) + "-" + ''.join(choice(sym_rng) for _ in range(5)) + "\n"  # thanks stackoverflow
        count = count + 1
    await save(f"\nGenerated at {ctime()}")
    await save(result)

    donefor = round(time() - start_time, 2)
    if donefor >= 0.01:
        await save(f"Done for {donefor} seconds")
    else:
        await save("Done!")


async def menu_2():
    print('Login required. I recommend using your main account here ONLY if you trust thirdparty "steam" library.')
    await login()
    while True:
        await activate_key(await generate_key())
        sleep(1)
