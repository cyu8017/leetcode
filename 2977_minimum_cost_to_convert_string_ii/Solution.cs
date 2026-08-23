// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

using System.Collections.Generic;

public class Solution {
    public long MinimumCost(string source, string target, string[] original, string[] changed, int[] cost) {
        const long inf = 1L << 60;
        var ids = new Dictionary<string, int>();
        int Id(string s) {
            if (ids.TryGetValue(s, out int v)) return v;
            v = ids.Count;
            ids[s] = v;
            return v;
        }
        for (int i = 0; i < original.Length; i++) {
            Id(original[i]);
            Id(changed[i]);
        }
        int m = ids.Count;
        long[][] dist = new long[m][];
        for (int i = 0; i < m; i++) {
            dist[i] = new long[m];
            for (int j = 0; j < m; j++) dist[i][j] = inf;
            dist[i][i] = 0;
        }
        for (int i = 0; i < original.Length; i++) {
            int u = Id(original[i]), v = Id(changed[i]);
            long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < m; k++)
            for (int i = 0; i < m; i++)
                for (int j = 0; j < m; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        int n = source.Length;
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = inf;
        dp[0] = 0;
        var lens = new HashSet<int>();
        foreach (var kv in ids) lens.Add(kv.Key.Length);
        for (int i = 0; i < n; i++) {
            if (dp[i] >= inf / 2) continue;
            if (source[i] == target[i] && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            foreach (int L in lens) {
                if (i + L > n) continue;
                string ss = source.Substring(i, L), tt = target.Substring(i, L);
                if (!ids.TryGetValue(ss, out int iu) || !ids.TryGetValue(tt, out int iv)) continue;
                if (dist[iu][iv] < inf / 2) {
                    long cand = dp[i] + dist[iu][iv];
                    if (cand < dp[i + L]) dp[i + L] = cand;
                }
            }
        }
        if (dp[n] >= inf / 2) return -1;
        return dp[n];
    }
}
