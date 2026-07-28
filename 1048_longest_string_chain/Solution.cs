// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

using System;
using System.Collections.Generic;

public class Solution {
    public int LongestStrChain(string[] words) {
        Array.Sort(words, (a, b) => a.Length.CompareTo(b.Length));
        var dp = new Dictionary<string, int>();
        int ans = 1;
        foreach (string w in words) {
            int best = 1;
            for (int i = 0; i < w.Length; i++) {
                string prev = w.Remove(i, 1);
                if (dp.TryGetValue(prev, out int v)) best = Math.Max(best, v + 1);
            }
            dp[w] = best;
            ans = Math.Max(ans, best);
        }
        return ans;
    }
}
