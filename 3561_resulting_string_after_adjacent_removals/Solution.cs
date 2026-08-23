// LeetCode 3561 - Resulting String After Adjacent Removals
// https://leetcode.com/problems/resulting-string-after-adjacent-removals/

using System;
using System.Text;

public class Solution {
    public string ResultingString(string s) {
        bool IsContiguous(char a, char b) {
            int x = Math.Abs(a - b);
            return x == 1 || x == 25;
        }
        var stk = new StringBuilder();
        foreach (char c in s) {
            if (stk.Length > 0 && IsContiguous(stk[stk.Length - 1], c)) stk.Length--;
            else stk.Append(c);
        }
        return stk.ToString();
    }
}
