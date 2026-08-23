// LeetCode 3575 - Maximum Good Subtree Score
// https://leetcode.com/problems/maximum-good-subtree-score/

using System;
using System.Collections.Generic;

public class Solution {
    public int GoodSubtreeSum(int[] vals, int[] par) {
        const int MOD = 1000000007;
        int n = vals.Length;
        var g = new List<int>[n];
        for (int i = 0; i < n; i++) g[i] = new List<int>();
        for (int i = 1; i < n; i++) g[par[i]].Add(i);
        int ans = 0;
        (int mask, bool ok, int v) DigitMask(int x) {
            int v = x, mask = 0;
            if (x == 0) return (1, true, 0);
            while (x > 0) {
                int d = x % 10;
                if ((mask & (1 << d)) != 0) return (0, false, 0);
                mask |= 1 << d;
                x /= 10;
            }
            return (mask, true, v);
        }
        Dictionary<int, int> Dfs(int u) {
            var dp = new Dictionary<int, int> { [0] = 0 };
            var (mask, ok, v) = DigitMask(vals[u]);
            if (ok) dp[mask] = v;
            foreach (int c in g[u]) {
                var child = Dfs(c);
                var ndp = new Dictionary<int, int>();
                foreach (var kv1 in dp) {
                    foreach (var kv2 in child) {
                        if ((kv1.Key & kv2.Key) == 0) {
                            int nm = kv1.Key | kv2.Key;
                            int ns = kv1.Value + kv2.Value;
                            if (!ndp.ContainsKey(nm) || ndp[nm] < ns) ndp[nm] = ns;
                        }
                    }
                }
                foreach (var kv in dp) {
                    if (!ndp.ContainsKey(kv.Key) || ndp[kv.Key] < kv.Value) ndp[kv.Key] = kv.Value;
                }
                foreach (var kv in child) {
                    if (!ndp.ContainsKey(kv.Key) || ndp[kv.Key] < kv.Value) ndp[kv.Key] = kv.Value;
                }
                dp = ndp;
            }
            int best = 0;
            foreach (var kv in dp) best = Math.Max(best, kv.Value);
            ans = (ans + best) % MOD;
            return dp;
        }
        Dfs(0);
        return ans;
    }
}
