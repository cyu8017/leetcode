// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

using System;

public class Solution {
    public int MaxDepth(string s) {
        int depth = 0, ans = 0;
        foreach (char ch in s) {
            if (ch == '(') {
                depth++;
                ans = Math.Max(ans, depth);
            } else if (ch == ')') {
                depth--;
            }
        }
        return ans;
    }
}
