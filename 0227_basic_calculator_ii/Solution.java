// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new ArrayDeque<>();
        int number = 0;
        char operator = '+';

        for (int index = 0; index < s.length(); index++) {
            char ch = s.charAt(index);
            if (Character.isDigit(ch)) {
                number = number * 10 + (ch - '0');
            }
            if (ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == s.length() - 1) {
                if (operator == '+') {
                    stack.push(number);
                } else if (operator == '-') {
                    stack.push(-number);
                } else if (operator == '*') {
                    stack.push(stack.pop() * number);
                } else if (operator == '/') {
                    stack.push(stack.pop() / number);
                }
                operator = ch;
                number = 0;
            }
        }

        int total = 0;
        for (int value : stack) {
            total += value;
        }
        return total;
    }
}
