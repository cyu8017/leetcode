// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

import java.util.*;

class Solution {
    public String reverseParentheses(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        for (char ch : s.toCharArray()) {
            if (ch == ')') {
                List<Character> chunk = new ArrayList<>();
                while (!stack.isEmpty() && stack.peek() != '(') chunk.add(stack.pop());
                stack.pop();
                for (char c : chunk) stack.push(c);
            } else stack.push(ch);
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) sb.append(stack.removeLast());
        return sb.toString();
    }
}
