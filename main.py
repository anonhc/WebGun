import argparse
import asyncio
import concurrent.futures
import tracemalloc

from dir_brute import *

tracemalloc.start()

parser = argparse.ArgumentParser()
parser.add_argument("--url", '-u', help="The URL to scan")
parser.add_argument("--ch", '-c', help="The Characters Used In The BruteForce")
parser.add_argument("--length", "-l", help="The Length of Characters ex. '6' ")
args = parser.parse_args()

if not args.url:
    parser.error("Please specify a URL")
    exit()
elif not args.ch:
    parser.error("Please specify a The Characters used in bruteforce")
    exit()
elif not args.length:
    parser.error("Please specify the length")
    exit()

def banner():
    with open("banner") as file:
        print(file.read())


def main():
    banner()
    target = args.url
    asyncio.run(dir_brute(ln=args.length, ch=args.ch, target=target))
    with concurrent.futures.ThreadPoolExecutor() as tpy:
        result = [tpy.submit(asyncio.run, dir_brute, ln=args.length, ch=args.ch, target=target)]
        for f in concurrent.futures.as_completed(result):
            print(f.result())


main()
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
