// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

using System.Text;

public class Solution {
    public bool IsPrefixString(string s, string[] words) {
        var sb = new StringBuilder();
        foreach (var w in words) {
            sb.Append(w);
            string cur = sb.ToString();
            if (cur == s) return true;
            if (cur.Length > s.Length || !s.StartsWith(cur)) return false;
        }
        return false;
    }
}