//imports
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System;
using System.IO;

namespace CSharp
{
    static class Day2
    {
        static readonly string[] inputs = File.ReadAllLines(Path.GetFullPath(Path.Combine(Directory.GetCurrentDirectory() + "..\\..\\..\\..\\inputs\\day2.txt")), Encoding.UTF8);

        public static void part1()
        {
            //What do you get if you multiply your final horizontal position by your final depth?

            int horizontalPos = 0;
            int depth = 0;

            for (int i = 0; i < inputs.Length; i++)
            {
                string command = inputs[i].Split(" ")[0];
                int value = int.Parse(inputs[i].Split(" ")[1]);
                //Console.WriteLine(String.Format("{0} {1}",command, value));

                if (command == "forward") 
                {
                    horizontalPos += value;
                }
                else if (command == "down")
                {
                    depth += value;
                }
                else
                {
                    depth -= value;
                }
            }
            
            Console.WriteLine(String.Format("What do you get if you multiply your final horizontal position by your final depth?\n{0}", horizontalPos * depth));
        }

        public static void part2()
        {
            //What do you get if you multiply your final horizontal position by your final depth?

            //Console.WriteLine(String.Format("\nWhat do you get if you multiply your final horizontal position by your final depth?\n{0}", increased));
        }

    }
}