// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

using System;
using System.Text;

public class Solution {
    public string ProcessStr(string s) {
        var result = new StringBuilder();
        foreach (char c in s) {
            if (char.IsLetter(c)) result.Append(c);
            else if (c == '*') {
                if (result.Length > 0) result.Length--;
            } else if (c == '#') result.Append(result.ToString());
            else if (c == '%') {
                char[] arr = result.ToString().ToCharArray();
                Array.Reverse(arr);
                result.Clear();
                result.Append(arr);
            }
        }
        return result.ToString();
    }
}
