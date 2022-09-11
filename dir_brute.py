import itertools
import aiohttp
from colorama import Fore


async def dir_brute(ln, ch, target):
    data = list(map("".join, itertools.product(f'{ch}', repeat=int(ln))))
    data.sort()
    i = 0
    while data:
        tg = f'{target}/{data[i]}'
        async with aiohttp.ClientSession() as session:
            await session.get(tg)
            async with session.get(tg) as resp:
                if resp.status != 404:
                    print(Fore.GREEN + f'[ + ] Found Site: {tg} ' + Fore.RESET + f' status_code:{resp.status}')
                    data.pop(i)
                    i += 1
