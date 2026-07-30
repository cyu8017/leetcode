// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string ReverseParentheses(string s) {
        var stack = new Stack<char>();
        foreach (char ch in s) {
            if (ch == ')') {
                var chunk = new List<char>();
                while (stack.Count > 0 && stack.Peek() != '(') chunk.Add(stack.Pop());
                stack.Pop();
                chunk.Reverse();
                foreach (char c in chunk) stack.Push(c);
            } else {
                stack.Push(ch);
            }
        }
        var sb = new StringBuilder(stack.Count);
        foreach (char ch in stack) sb.Append(ch);
        return sb.ToString();
    }
}
