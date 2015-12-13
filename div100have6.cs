using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace testApp
{
    class Program
    {
        public static bool test6(int val)
        {
            bool ret = Convert.ToString(val).IndexOf("6") >= 0;
            if (ret)
            {
                int i = 0;
            }
            return ret;
        }
        public static bool test(int i1, int i2, int i3, int i4, int i5, int i6, int i7)
        {
            bool cond1 = i1 + i2 + i3 + i4 + i5 + i6 + i7 == 100;
            /*bool condHaveSix1 = Convert.ToString(i1).IndexOf("6") >= 0;
            bool condHaveSix2 = Convert.ToString(i2).IndexOf("6") >= 0;
            bool condHaveSix3 = Convert.ToString(i3).IndexOf("6") >= 0;
            bool condHaveSix4 = Convert.ToString(i4).IndexOf("6") >= 0;
            bool condHaveSix5 = Convert.ToString(i5).IndexOf("6") >= 0;
            bool condHaveSix6 = Convert.ToString(i6).IndexOf("6") >= 0;
            bool condHaveSix7 = Convert.ToString(i7).IndexOf("6") >= 0;/**/
            if (cond1
               /* && condHaveSix1
                &&   condHaveSix2
                &&   condHaveSix3
                &&   condHaveSix4
                &&   condHaveSix5
                &&   condHaveSix6
                && condHaveSix7/**/
                )
            {
                return true;
            }
            return false;
        }
        public static string pack_as_string(int i1, int i2, int i3, int i4, int i5, int i6, int i7)
        {
            List<int> lst = new List<int>();
            lst.Add(i1);
            lst.Add(i2);
            lst.Add(i3);
            lst.Add(i4);
            lst.Add(i5);
            lst.Add(i6);
            lst.Add(i7);

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
            int len = 65;
            for (int i1 = 0; i1 < len; i1++)
            {
                if (!test6(i1))
                    continue;

                for (int i2 = 0; i2 < len; i2++)
                {
                    if (!test6(i2))
                        continue;
                    for (int i3 = 0; i3 < len; i3++)
                    {
                        if (!test6(i3))
                            continue;
                        for (int i4 = 0; i4 < len; i4++)
                        {
                            if (!test6(i4))
                                continue;
                            for (int i5 = 0; i5 < len; i5++)
                            {
                                if (!test6(i5))
                                    continue;
                                for (int i6 = 0; i6 < len; i6++)
                                {
                                    if (!test6(i6))
                                        continue;
                                    for (int i7 = 0; i7 < len; i7++)
                                    {
                                        if (!test6(i7))
                                            continue;
                                        if (test(i1, i2, i3, i4, i5, i6, i7))
                                        {
                                            string str = pack_as_string(i1, i2, i3, i4, i5, i6, i7);
                                            if (lst.IndexOf(str) < 0)
                                            {
                                                lst.Add(str);
                                            }
                                        }
                                    }
                                }
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
