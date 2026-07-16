// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Map;

class Solution {
    public boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        Map<Character, Character> pairs = Map.of(')', '(', ']', '[', '}', '{');

        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.push(ch);
            } else if (stack.isEmpty() || stack.pop() != pairs.get(ch)) {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
