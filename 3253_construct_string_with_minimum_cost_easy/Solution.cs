// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

using System.Collections.Generic;

public class Solution {
    public int MinimumCost(string target, string[] words, int[] costs) {
        const long inf = (long)1e18;
        int n = target.Length;
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = inf;
        dp[0] = 0;
        var best = new Dictionary<string, int>();
        for (int i = 0; i < words.Length; i++) {
            if (!best.ContainsKey(words[i]) || costs[i] < best[words[i]]) best[words[i]] = costs[i];
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            foreach (var kv in best) {
                string w = kv.Key;
                int c = kv.Value;
                int L = w.Length;
                if (i + L <= n && target.Substring(i, L) == w && dp[i] + c < dp[i + L]) {
                    dp[i + L] = dp[i] + c;
                }
            }
        }
        if (dp[n] == inf) return -1;
        return (int)dp[n];
    }
}
