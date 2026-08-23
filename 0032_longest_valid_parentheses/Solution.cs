// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

public class Solution {
    public int LongestValidParentheses(string s) {
        var stack = new Stack<int>();
        stack.Push(-1);
        int best = 0;

        for (int i = 0; i < s.Length; i++) {
            if (s[i] == '(') {
                stack.Push(i);
            } else {
                stack.Pop();
                if (stack.Count == 0) {
                    stack.Push(i);
                } else {
                    best = Math.Max(best, i - stack.Peek());
                }
            }
        }

        return best;
    }
}
