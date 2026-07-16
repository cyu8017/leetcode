// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

using System.Collections.Generic;

public class Solution {
    public int Calculate(string s) {
        var stack = new Stack<int>();
        int number = 0;
        char operatorChar = '+';

        for (int index = 0; index < s.Length; index++) {
            char ch = s[index];
            if (char.IsDigit(ch)) {
                number = number * 10 + (ch - '0');
            }
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == s.Length - 1) {
                if (operatorChar == '+') {
                    stack.Push(number);
                } else if (operatorChar == '-') {
                    stack.Push(-number);
                } else if (operatorChar == '*') {
                    stack.Push(stack.Pop() * number);
                } else if (operatorChar == '/') {
                    stack.Push(stack.Pop() / number);
                }
                operatorChar = ch;
                number = 0;
            }
        }

        int total = 0;
        foreach (int value in stack) {
            total += value;
        }
        return total;
    }
}
