// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string ReformatNumber(string number) {
        var s = new string(number.Where(char.IsDigit).ToArray());
        var parts = new List<string>();
        while (s.Length > 4) {
            parts.Add(s[..3]);
            s = s[3..];
        }
        if (s.Length == 4) {
            parts.Add(s[..2]);
            parts.Add(s[2..]);
        } else if (s.Length > 0) {
            parts.Add(s);
        }
        return string.Join("-", parts);
    }
}
