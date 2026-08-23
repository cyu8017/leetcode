// LeetCode 0828 - Count Unique Characters of All Substrings of a Given String
// https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/

using System.Collections.Generic;

public class Solution {
    public int UniqueLetterString(string s) {
        int n = s.Length;
        var last = new Dictionary<char, List<int>>();
        foreach (char ch in s) {
            if (!last.ContainsKey(ch)) last[ch] = new List<int> { -1 };
        }
        for (int i = 0; i < n; i++) last[s[i]].Add(i);
        foreach (var indices in last.Values) indices.Add(n);
        int ans = 0;
        foreach (var indices in last.Values) {
            for (int k = 1; k + 1 < indices.Count; k++)
                ans += (indices[k] - indices[k - 1]) * (indices[k + 1] - indices[k]);
        }
        return ans;
    }
}
