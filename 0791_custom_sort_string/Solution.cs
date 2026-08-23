// LeetCode 0791 - Custom Sort String
// https://leetcode.com/problems/custom-sort-string/

using System.Text;

public class Solution {
    public string CustomSortString(string order, string s) {
        int[] counts = new int[26];
        foreach (char ch in s) counts[ch - 'a']++;
        var sb = new StringBuilder();
        foreach (char ch in order) {
            while (counts[ch - 'a'] > 0) { sb.Append(ch); counts[ch - 'a']--; }
        }
        for (int i = 0; i < 26; i++) {
            while (counts[i] > 0) { sb.Append((char)('a' + i)); counts[i]--; }
        }
        return sb.ToString();
    }
}
