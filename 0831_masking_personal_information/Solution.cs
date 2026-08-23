// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

using System.Text;

public class Solution {
    public string MaskPII(string s) {
        int at = s.IndexOf('@');
        if (at >= 0) {
            s = s.ToLowerInvariant();
            at = s.IndexOf('@');
            string name = s.Substring(0, at);
            string domain = s.Substring(at + 1);
            return name[0] + "*****" + name[^1] + "@" + domain;
        }
        var digits = new StringBuilder();
        foreach (char ch in s) if (char.IsDigit(ch)) digits.Append(ch);
        string d = digits.ToString();
        string local = d.Substring(d.Length - 4);
        int country = d.Length - 10;
        if (country == 0) return "***-***-" + local;
        return "+" + new string('*', country) + "-***-***-" + local;
    }
}
