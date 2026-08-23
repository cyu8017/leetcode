// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumOperationsToMakeKPeriodic(string word, int k) {
        var cnt = new Dictionary<string, int>();
        int n = word.Length, mx = 0;
        for (int i = 0; i < n; i += k) {
            string s = word.Substring(i, k);
            if (!cnt.ContainsKey(s)) cnt[s] = 0;
            mx = Math.Max(mx, ++cnt[s]);
        }
        return n / k - mx;
    }
}
