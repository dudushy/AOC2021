#imports
import os.path as Path

# set global path
path = Path.join(Path.dirname(__file__), 'inputs\\day2.txt')

#main
def part1():
    global path
    with open(path, 'r') as file:
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
    global path
    with open(path, 'r') as file:
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
    main()