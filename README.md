<h1><a href="https://adventofcode.com/2021">Advent Of Code 2021</a></h1>

Day | Status
--- | --- 
1 [py](https://github.com/dudushy/AOC2021/blob/main/Python/day1.py), [cs](https://github.com/dudushy/AOC2021/blob/main/CSharp/day1.cs) | :heavy_check_mark:
2 [py](https://github.com/dudushy/AOC2021/blob/main/Python/day2.py), [cs](https://github.com/dudushy/AOC2021/blob/main/CSharp/day2.cs) | :heavy_check_mark:
3 | :x:
4 | :x:
5 | :x:
6 | :x:
7 | :x:
8 | :x:
9 | :x:
10 | :x:
11 | :x:
12 | :x:
13 | :x:
14 | :x:
15 | :x:
16 | :x:
17 | :x:
18 | :x:
19 | :x:
20 | :x:
21 | :x:
22 | :x:
23 | :x:
24 | :x:
25 | :x:

---
## Python Template
```py
# Imports
import os.path as Path

# Set global path
path = Path.join(Path.dirname(__file__), 'dayX.txt')

# Main
def part1():
    global path
    with open(path, 'r') as file:
        # PART 1 HERE

def part2():
    global path
    with open(path, 'r') as file:
        # PART 2 HERE

def main():
    part1()
    part2()

if __name__ == "__main__":
    main()
```

## C# Template
```cs
// Imports
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// Main
namespace CSharp
{
    static class DayX
    {
        // Set global path
        static readonly string[] inputs = File.ReadAllLines(Path.GetFullPath(Path.Combine(Directory.GetCurrentDirectory() + "..\\..\\..\\..\\inputs\\dayX.txt")), Encoding.UTF8);

        public static void Part1()
        {
            //PART 1 HERE
        }

        public static void Part2()
        {
            //PART 2 HERE
        }

    }
}
```
