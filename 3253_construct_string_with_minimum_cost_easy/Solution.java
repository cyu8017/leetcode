// LeetCode 3253 - Construct String with Minimum Cost (Easy)
// https://leetcode.com/problems/construct-string-with-minimum-cost-easy/

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int minimumCost(String target, String[] words, int[] costs) {
        final long inf = (long) 1e18;
        int n = target.length();
        long[] dp = new long[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = inf;
        dp[0] = 0;
        Map<String, Integer> best = new HashMap<>();
        for (int i = 0; i < words.length; i++) {
            Integer old = best.get(words[i]);
            if (old == null || costs[i] < old) best.put(words[i], costs[i]);
        }
        for (int i = 0; i < n; i++) {
            if (dp[i] == inf) continue;
            for (Map.Entry<String, Integer> e : best.entrySet()) {
                String w = e.getKey();
                int c = e.getValue();
                int L = w.length();
                if (i + L <= n && target.startsWith(w, i) && dp[i] + c < dp[i + L]) {
                    dp[i + L] = dp[i] + c;
                }
            }
        }
        if (dp[n] == inf) return -1;
        return (int) dp[n];
    }
}
