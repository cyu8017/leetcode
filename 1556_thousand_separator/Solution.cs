// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

using System.Collections.Generic;

public class Solution {
    public string ThousandSeparator(int n) {
        string s = n.ToString();
        var parts = new List<string>();
        while (s.Length > 0) {
            int take = s.Length >= 3 ? 3 : s.Length;
            parts.Add(s.Substring(s.Length - take));
            s = s.Substring(0, s.Length - take);
        }
        parts.Reverse();
        return string.Join(".", parts);
    }
}
