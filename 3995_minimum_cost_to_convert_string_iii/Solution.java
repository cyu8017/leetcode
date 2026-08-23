// LeetCode 3995 - Minimum Cost to Convert String III
// https://leetcode.com/problems/minimum-cost-to-convert-string-iii/

class Solution {
    public int minCost(String source, String target, String[][] rules, int[] costs) {
        int n = source.length();
        if (target.length() != n) return -1;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = Integer.MAX_VALUE;
        dp[0] = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == Integer.MAX_VALUE) continue;
            if (source.charAt(i) == target.charAt(i) && dp[i] < dp[i + 1]) dp[i + 1] = dp[i];
            for (int j = 0; j < rules.length; j++) {
                String p = rules[j][0];
                String r = rules[j][1];
                int plen = p.length();
                if (i + plen > n) continue;
                int c = costs[j];
                boolean ok = true;
                for (int k = 0; k < plen; k++) {
                    if (r.charAt(k) != target.charAt(i + k)) { ok = false; break; }
                    if (p.charAt(k) == '*') ++c;
                    else if (p.charAt(k) != source.charAt(i + k)) { ok = false; break; }
                }
                if (ok && dp[i] <= Integer.MAX_VALUE - c && dp[i] + c < dp[i + plen]) {
                    dp[i + plen] = dp[i] + c;
                }
            }
        }
        return dp[n] == Integer.MAX_VALUE ? -1 : dp[n];
    }
}
