// LeetCode 0394 - Decode String

// https://leetcode.com/problems/decode-string/



using System.Collections.Generic;

using System.Text;



public class Solution {

    public string DecodeString(string s) {

        Stack<(string previous, int count)> stack = new();

        StringBuilder current = new();

        int number = 0;



        foreach (char character in s) {

            if (char.IsDigit(character)) {

                number = number * 10 + (character - '0');

            } else if (character == '[') {

                stack.Push((current.ToString(), number));

                current.Clear();

                number = 0;

            } else if (character == ']') {

                var (previous, count) = stack.Pop();

                StringBuilder repeated = new();

                for (int repeat = 0; repeat < count; repeat++) {

                    repeated.Append(current);

                }

                current = new StringBuilder(previous).Append(repeated);

            } else {

                current.Append(character);

            }

        }



        return current.ToString();

    }

}
