// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        var pairs = new Dictionary<char, char> {
            [')'] = '(',
            [']'] = '[',
            ['}'] = '{',
        };

        foreach (char ch in s) {
            if (ch == '(' || ch == '[' || ch == '{') {
                stack.Push(ch);
            } else if (stack.Count == 0 || stack.Pop() != pairs[ch]) {
                return false;
            }
        }

        return stack.Count == 0;
    }
}
