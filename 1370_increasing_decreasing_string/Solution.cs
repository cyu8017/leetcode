// LeetCode 1370 - Increasing Decreasing String
// https://leetcode.com/problems/increasing-decreasing-string/

using System.Text;
public class Solution {
    public string SortString(string s) {
        var c = new int[26];
        foreach (char ch in s) c[ch - 'a']++;
        var sb = new StringBuilder();
        while (sb.Length < s.Length) {
            for (int i = 0; i < 26; i++) if (c[i]-- > 0) sb.Append((char)('a' + i)); else c[i]++;
            for (int i = 25; i >= 0; i--) if (c[i]-- > 0) sb.Append((char)('a' + i)); else c[i]++;
        }
        return sb.ToString();
    }
}
