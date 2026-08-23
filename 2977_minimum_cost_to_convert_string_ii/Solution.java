// LeetCode 2977 - Minimum Cost to Convert String II
// https://leetcode.com/problems/minimum-cost-to-convert-string-ii/

import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

class Solution {
    public long minimumCost(String source, String target, String[] original, String[] changed, int[] cost) {
        final long INF = 1L << 60;
        Map<String, Integer> ids = new HashMap<>();
        for (int i = 0; i < original.length; i++) {
            ids.putIfAbsent(original[i], ids.size());
            ids.putIfAbsent(changed[i], ids.size());
        }
        int m = ids.size();
        long[][] dist = new long[m][m];
        for (int i = 0; i < m; i++) {
            Arrays.fill(dist[i], INF);
            dist[i][i] = 0;
        }
        for (int i = 0; i < original.length; i++) {
            int u = ids.get(original[i]), v = ids.get(changed[i]);
            long ww = cost[i];
            if (ww < dist[u][v]) dist[u][v] = ww;
        }
        for (int k = 0; k < m; k++)
            for (int i = 0; i < m; i++)
                for (int j = 0; j < m; j++)
                    if (dist[i][k] + dist[k][j] < dist[i][j])
                        dist[i][j] = dist[i][k] + dist[k][j];
        int n = source.length();
        long[] dp = new long[n + 1];
        Arrays.fill(dp, INF);
        dp[0] = 0;
        Set<Integer> lens = new HashSet<>();
        for (String key : ids.keySet()) lens.add(key.length());
        for (int i = 0; i < n; i++) {
            if (dp[i] >= INF / 2) continue;
            if (source.charAt(i) == target.charAt(i) && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int L : lens) {
                if (i + L > n) continue;
                String ss = source.substring(i, i + L), tt = target.substring(i, i + L);
                Integer iu = ids.get(ss), iv = ids.get(tt);
                if (iu == null || iv == null) continue;
                if (dist[iu][iv] < INF / 2) {
                    long cand = dp[i] + dist[iu][iv];
                    if (cand < dp[i + L]) dp[i + L] = cand;
                }
            }
        }
        if (dp[n] >= INF / 2) return -1;
        return dp[n];
    }
}
