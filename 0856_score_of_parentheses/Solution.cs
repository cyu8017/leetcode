// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

using System;
using System.Collections.Generic;

public class Solution {
    public int ScoreOfParentheses(string s) {
        var stack = new List<int> { 0 };
        foreach (char ch in s) {
            if (ch == '(') stack.Add(0);
            else {
                int val = stack[stack.Count - 1];
                stack.RemoveAt(stack.Count - 1);
                stack[stack.Count - 1] += Math.Max(2 * val, 1);
            }
        }
        return stack[0];
    }
}
