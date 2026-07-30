// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

using System.Collections.Generic;
using System.Text;
public class Solution {
    public string Reformat(string s) {
        var letters = new List<char>(); var digits = new List<char>();
        foreach (char c in s) if (char.IsLetter(c)) letters.Add(c); else digits.Add(c);
        if (System.Math.Abs(letters.Count - digits.Count) > 1) return "";
        if (digits.Count > letters.Count) { var t = letters; letters = digits; digits = t; }
        var sb = new StringBuilder();
        for (int i = 0; i < letters.Count; i++) {
            sb.Append(letters[i]);
            if (i < digits.Count) sb.Append(digits[i]);
        }
        return sb.ToString();
    }
}
