// LeetCode 0402 - Remove K Digits

// https://leetcode.com/problems/remove-k-digits/



using System.Collections.Generic;

using System.Text;



public class Solution {

    public string RemoveKdigits(string num, int k) {

        Stack<char> stack = new();



        foreach (char digit in num) {

            while (k > 0 && stack.Count > 0 && stack.Peek() > digit) {

                stack.Pop();

                k--;

            }

            stack.Push(digit);

        }



        while (k > 0 && stack.Count > 0) {

            stack.Pop();

            k--;

        }



        StringBuilder result = new();

        foreach (char digit in stack) {

            result.Insert(0, digit);

        }



        int start = 0;

        while (start < result.Length && result[start] == '0') {

            start++;

        }



        if (start == result.Length) {

            return "0";

        }



        return result.ToString(start, result.Length - start);

    }

}
