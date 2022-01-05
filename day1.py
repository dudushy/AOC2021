#imports
import os

# set global path
path = os.path.dirname(__file__)

#main
def part1():
    global path
    with open(f'{path}\day1.txt', 'r') as file:
        last_input = float("inf")
        increased = 0
        decreased = 0
        for item in file:
            item = int(item.strip())
            if item > last_input:
                increased += 1
            else:
                decreased += 1
            last_input = item
        print(f"\nHow many measurements are larger than the previous measurement?\n{increased}")

def part2():
    global path
    with open(f'{path}\day1.txt', 'r') as file:
        last_input = float("inf")
        increased = 0
        decreased = 0
        items = []
        for item in file:
            item = int(item.strip())
            items.append(item)
        for i in range(len(items) - 2):
            value = sum(items[i:i+3])
            if value > last_input:
                increased += 1
            else:
                decreased += 1
            last_input = value
        print(f"\nHow many sums are larger than the previous sum?\n{increased}")

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()