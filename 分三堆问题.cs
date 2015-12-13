using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testApp
{
    class Program
    {
        public static bool test(int a, int b, int c)
        {
            if (a + b + c == 12 
                && a != b 
                && b != c 
                && a != c
                && a>0
                && b>0
                && c>0
                )
            {
                return true;
            }
            return false;
        }
        public static string pack_as_string(int a, int b, int c)
        {
            List<int> lst = new List<int>();
            lst.Add(a);
            lst.Add(b);
            lst.Add(c);

            lst.Sort();
            
            string str = "";
            foreach (var item in lst)
            {
                str +=item +" ";
            }
            return str;
        }

        static void Main(string[] args)
        {
            List<string> lst = new List<string>();
            int len = 10;
            for (int i = 0; i < len; i++)
            {
                for (int j = 0; j < len; j++)
                {
                    for (int k = 0; k < len; k++)
                    {
                        if (test(i, j, k))
                        {
                            string str = pack_as_string(i, j, k);
                            if (lst.IndexOf(str) < 0)
                            {
                                lst.Add(str);
                            }
                        }
                    }
                }
            }
            
            Console.WriteLine("共有" + Convert.ToString(lst.Count) + "种方法:");
            foreach (var item in lst)
            {
                Console.WriteLine(item);
            }
        }
    }
}
