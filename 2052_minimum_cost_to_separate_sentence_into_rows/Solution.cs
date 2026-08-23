// LeetCode 2052 - Minimum Cost to Separate Sentence Into Rows
// https://leetcode.com/problems/minimum-cost-to-separate-sentence-into-rows/

using System;

public class Solution {
    public int MinimumCost(string sentence, int k) {
        var words = sentence.Split(' ', StringSplitOptions.RemoveEmptyEntries);
        int n = words.Length;
        long INF = (long)1e18;
        long[] dp = new long[n + 1];
        Array.Fill(dp, INF);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; i--) {
            int length = -1;
            for (int j = i; j < n; j++) {
                length += 1 + words[j].Length;
                if (length > k) break;
                long cost = 0;
                if (j < n - 1) {
                    long extra = k - length;
                    cost = extra * extra;
                }
                dp[i] = Math.Min(dp[i], cost + dp[j + 1]);
            }
        }
        return (int)dp[0];
    }
}
