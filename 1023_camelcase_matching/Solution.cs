// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

using System.Collections.Generic;

public class Solution {
    public IList<bool> CamelMatch(string[] queries, string pattern) {
        var ans = new List<bool>();
        foreach (string q in queries) ans.Add(Matches(q, pattern));
        return ans;
    }

    private static bool Matches(string q, string pattern) {
        int i = 0;
        foreach (char ch in q) {
            if (i < pattern.Length && ch == pattern[i]) i++;
            else if (char.IsUpper(ch)) return false;
        }
        return i == pattern.Length;
    }
}
