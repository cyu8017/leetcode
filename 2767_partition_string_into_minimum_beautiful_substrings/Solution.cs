// LeetCode 2767 - Partition String Into Minimum Beautiful Substrings
// https://leetcode.com/problems/partition-string-into-minimum-beautiful-substrings/

using System;
using System.Collections.Generic;

public class Solution {
    public int MinimumBeautifulSubstrings(string s) {
        int n = s.Length;
        var pow5 = new HashSet<string>();
        for (long x = 1; ; x *= 5) {
            string b = "";
            long t = x;
            while (t > 0) { b = ((char)('0' + (t & 1))) + b; t >>= 1; }
            if (b.Length == 0) b = "0";
            if (b.Length > n) break;
            pow5.Add(b);
        }
        const int INF = 1 << 30;
        int[] dp = new int[n + 1];
        Array.Fill(dp, INF);
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == INF || s[i] == '0') continue;
            for (int j = i + 1; j <= n; j++) {
                if (pow5.Contains(s.Substring(i, j - i)))
                    dp[j] = Math.Min(dp[j], dp[i] + 1);
            }
        }
        return dp[n] == INF ? -1 : dp[n];
    }
}
