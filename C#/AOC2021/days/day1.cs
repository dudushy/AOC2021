using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace ConsoleApp1
{
    static class day1
    {
        static void Main(string[] args)
        {
            Part1();
        }

        static void Part1()
        {
            //How many measurements are larger than the previous measurement?

            string[] inputs = File.ReadAllLines("C:\\Users\\User\\Documents\\DriveSync\\GitHub\\AOC2021\\C#\\AOC2021\\inputs\\day1.txt", Encoding.UTF8);
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

            Console.WriteLine(String.Format("How many measurements are larger than the previous measurement?\n{0}", increased));
        }

        static void Part2()
        {
            //How many sums are larger than the previous sum?
        }

    }
}