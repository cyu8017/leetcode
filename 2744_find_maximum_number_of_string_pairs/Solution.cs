// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumNumberOfStringPairs(string[] words) {
        var freq = new Dictionary<string, int>();
        int ans = 0;
        foreach (var w in words) {
            char[] ca = w.ToCharArray();
            Array.Reverse(ca);
            string rev = new string(ca);
            if (freq.TryGetValue(rev, out int c) && c > 0) {
                ans++;
                freq[rev] = c - 1;
            } else {
                if (!freq.ContainsKey(w)) freq[w] = 0;
                freq[w]++;
            }
        }
        return ans;
    }
}
