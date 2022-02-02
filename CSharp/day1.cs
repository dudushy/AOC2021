//imports
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSharp
{
    static class Day1
    {
        static readonly string[] inputs = File.ReadAllLines(Path.GetFullPath(Path.Combine(Directory.GetCurrentDirectory() + "..\\..\\..\\..\\inputs\\day1.txt")), Encoding.UTF8);

        public static void part1()
        {
            //How many measurements are larger than the previous measurement?

            float last_input = float.PositiveInfinity;
            int increased = 0;
            int decreased = 0;

            for (int i = 0; i < inputs.Length; i++)
            {
                if (int.Parse(inputs[i]) > last_input)
                {
                    increased += 1;
                }
                else
                {
                    decreased += 1;
                }
                last_input = int.Parse(inputs[i]);
            }

            Console.WriteLine(String.Format("\nHow many measurements are larger than the previous measurement?\n{0}", increased));
        }

        public static void part2()
        {
            //How many sums are larger than the previous sum?

            float last_input = float.PositiveInfinity;
            int increased = 0;
            int decreased = 0;
            int[] items = new int[inputs.Length];

            for (int i = 0; i < inputs.Length; i++)
            {
                items[i] = int.Parse(inputs[i]);
            }
            for (int k = 0; k < (items.Length - 2); k++)
            {
                int value = items[k..(k+3)].Sum();
                if (value > last_input)
                {
                    increased += 1;
                }
                else
                {
                    decreased += 1;
                }
                last_input = value;

            }
            Console.WriteLine(String.Format("\nHow many measurements are larger than the previous measurement?\n{0}", increased));
        }

    }
}