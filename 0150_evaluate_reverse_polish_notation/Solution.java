// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

import java.util.*;
class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> stack = new ArrayDeque<>();
        for (String token : tokens) {
            if ("+-*/".contains(token) && token.length() == 1) {
                int right = stack.pop(), left = stack.pop();
                switch (token) {
                    case "+": stack.push(left + right); break;
                    case "-": stack.push(left - right); break;
                    case "*": stack.push(left * right); break;
                    default: stack.push(left / right);
                }
            } else stack.push(Integer.parseInt(token));
        }
        return stack.pop();
    }
}