// LeetCode 1249 - Minimum Remove to Make Valid Parentheses
// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

import java.util.*;

class Solution {
    public String minRemoveToMakeValid(String s) {
        char[] chars = s.toCharArray();
        Deque<Integer> opens = new ArrayDeque<>();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] == '(') opens.push(i);
            else if (chars[i] == ')') {
                if (opens.isEmpty()) chars[i] = 0;
                else opens.pop();
            }
        }
        while (!opens.isEmpty()) chars[opens.pop()] = 0;
        StringBuilder sb = new StringBuilder();
        for (char ch : chars) if (ch != 0) sb.append(ch);
        return sb.toString();
    }
}

