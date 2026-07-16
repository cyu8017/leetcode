// LeetCode 0385 - Mini Parser

// https://leetcode.com/problems/mini-parser/



using System.Collections.Generic;



public class NestedInteger {

    private int? integer;

    private readonly List<NestedInteger> list = new();



    public NestedInteger() {

    }



    public NestedInteger(int value) {

        integer = value;

    }



    public bool IsInteger() {

        return integer.HasValue;

    }



    public int GetInteger() {

        return integer ?? 0;

    }



    public IList<NestedInteger> GetList() {

        return list;

    }

}



public class Solution {

    public NestedInteger Deserialize(string s) {

        if (s[0] != '[') {

            return new NestedInteger(int.Parse(s));

        }



        Stack<NestedInteger> stack = new();

        NestedInteger? current = null;

        int index = 0;

        bool negative = false;

        int number = 0;

        bool hasNumber = false;



        while (index < s.Length) {

            char ch = s[index];

            if (ch == '[') {

                NestedInteger item = new NestedInteger();

                if (current != null) {

                    stack.Push(current);

                }

                current = item;

            } else if (ch == '-') {

                negative = true;

            } else if (char.IsDigit(ch)) {

                number = number * 10 + (ch - '0');

                hasNumber = true;

            } else if (ch == ',' || ch == ']') {

                if (hasNumber) {

                    current!.GetList().Add(new NestedInteger(negative ? -number : number));

                    number = 0;

                    negative = false;

                    hasNumber = false;

                }

                if (ch == ']') {

                    if (stack.Count == 0) {

                        return current!;

                    }

                    NestedInteger parent = stack.Pop();

                    parent.GetList().Add(current!);

                    current = parent;

                }

            }

            index++;

        }



        return current ?? new NestedInteger();

    }

}
