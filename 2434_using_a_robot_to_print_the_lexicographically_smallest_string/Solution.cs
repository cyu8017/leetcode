// LeetCode 2434 - Using a Robot to Print the Lexicographically Smallest String
// https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

using System;
using System.Text;

public class Solution {
    public string RobotWithString(string s) {
        int n = s.Length;
        char[] minSuf = new char[n + 1];
        minSuf[n] = (char)('z' + 1);
        for (int i = n - 1; i >= 0; i--)
            minSuf[i] = s[i] < minSuf[i + 1] ? s[i] : minSuf[i + 1];
        var stack = new StringBuilder();
        var ans = new StringBuilder();
        for (int i = 0; i < n; i++) {
            stack.Append(s[i]);
            while (stack.Length > 0 && stack[stack.Length - 1] <= minSuf[i + 1]) {
                ans.Append(stack[stack.Length - 1]);
                stack.Length--;
            }
        }
        while (stack.Length > 0) {
            ans.Append(stack[stack.Length - 1]);
            stack.Length--;
        }
        return ans.ToString();
    }
}
