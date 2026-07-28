// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

using System.Collections.Generic;

public class Solution {
    public bool IsValid(string s) {
        var stack = new List<char>();
        foreach (char ch in s) {
            stack.Add(ch);
            int n = stack.Count;
            if (n >= 3 && stack[n - 3] == 'a' && stack[n - 2] == 'b' && stack[n - 1] == 'c') {
                stack.RemoveRange(n - 3, 3);
            }
        }
        return stack.Count == 0;
    }
}
