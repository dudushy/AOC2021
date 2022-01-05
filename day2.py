import os.path as Path
import httpx
from env import sessionCookie
inputFilePath = None

def part1():
    global inputFilePath
    with open(inputFilePath, 'r') as file:
        horizontalPos = 0
        depth = 0

        for item in file:
            command, value = item.split()
            if command == "forward":
                horizontalPos += int(value)
            elif command == "down":
                depth += int(value)
            else:
                depth -= int(value)

        print(f"\nWhat do you get if you multiply your final horizontal position by your final depth?\n{horizontalPos * depth}")

def part2():
    global inputFilePath
    with open(inputFilePath, 'r') as file:
        horizontalPos = 0
        depth = 0
        aim = 0

        for item in file:
            command, value = item.split()
            if command == "forward":
                horizontalPos += int(value)
                depth += (aim * int(value))
            elif command == "down":
                aim += int(value)
            else:
                aim -= int(value)

        print(f"\nWhat do you get if you multiply your final horizontal position by your final depth?\n{horizontalPos * depth}")



def main():
    part1()
    part2()

if __name__ == "__main__":
    day : int = 2
    path : str = Path.dirname(__file__)
    inputFilePath : str = Path.join(path, f"day{day}.txt")

    if not Path.exists(inputFilePath):
        print("Downloading input...")
        with open(inputFilePath, "w+") as file:
            with httpx.Client() as client:
                client.cookies.set("session", sessionCookie)
                file.write(client.get(f"https://adventofcode.com/2021/day/{day}/input").text)
    main()