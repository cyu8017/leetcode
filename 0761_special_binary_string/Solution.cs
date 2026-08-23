// LeetCode 0761 - Special Binary String
// https://leetcode.com/problems/special-binary-string/

using System.Collections.Generic;
using System.Text;

public class Solution {
    public string MakeLargestSpecial(string s) {
        var parts = new List<string>();
        int balance = 0, start = 0;
        for (int i = 0; i < s.Length; i++) {
            balance += s[i] == '1' ? 1 : -1;
            if (balance == 0) {
                parts.Add("1" + MakeLargestSpecial(s.Substring(start + 1, i - start - 1)) + "0");
                start = i + 1;
            }
        }
        parts.Sort((a, b) => string.CompareOrdinal(b, a));
        var result = new StringBuilder();
        foreach (string part in parts) result.Append(part);
        return result.ToString();
    }
}
