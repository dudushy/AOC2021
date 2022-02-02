#imports
import os.path as Path

# set global path
path = Path.join(Path.dirname(__file__), 'inputs\\day3.txt')

#main
def part1():
    global path
    with open(path, 'r') as file:
        gammaRate = 0
        epsilonRate = 0
        count1 = 0
        count0 = 0
        for line in file:
            for char in line:
                pass #enumerate

def part2():
    global path
    with open(path, 'r') as file:
        pass

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()