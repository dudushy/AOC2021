import os.path as Path
import httpx
from env import sessionCookie

def part1():
    pass


def part2():
    pass


def main():
    pass

if __name__ == "__main__":
    day : int = 1
    path : str = Path.dirname(__file__)
    inputFilePath : str = Path.join(path, f"day{day}.txt")

    if not Path.exists(inputFilePath):
        print("Downloading input...")
        with open(inputFilePath, "w+") as file:
            with httpx.Client() as client:
                client.cookies.set("session", sessionCookie)
                file.write(client.get(f"https://adventofcode.com/2021/day/{day}/input").text)
    main()