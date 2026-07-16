// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

using System.Collections.Generic;

public class Solution {
    public int Calculate(string s) {
        Stack<int> stack = new Stack<int>();
        int result = 0;
        int number = 0;
        int sign = 1;
        foreach (char ch in s) {
            if (char.IsDigit(ch)) {
                number = number * 10 + (ch - '0');
            } else if (ch == '+' || ch == '-') {
                result += sign * number;
                number = 0;
                sign = ch == '+' ? 1 : -1;
            } else if (ch == '(') {
                stack.Push(result);
                stack.Push(sign);
                result = 0;
                sign = 1;
            } else if (ch == ')') {
                result += sign * number;
                number = 0;
                result *= stack.Pop();
                result += stack.Pop();
            }
        }
        result += sign * number;
        return result;
    }
}
