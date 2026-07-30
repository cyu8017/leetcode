// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

using System.Text;

public class Solution {
    public string RemoveOccurrences(string s, string part) {
        var sb = new StringBuilder();
        int m = part.Length;
        foreach (char ch in s) {
            sb.Append(ch);
            if (sb.Length >= m && sb.ToString(sb.Length - m, m) == part)
                sb.Length -= m;
        }
        return sb.ToString();
    }
}