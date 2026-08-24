// LeetCode 0943 - Find the Shortest Superstring
// https://leetcode.com/problems/find-the-shortest-superstring/

class Solution {
    public String shortestSuperstring(String[] words) {
        int n = words.length;
        int[][] overlap = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) continue;
                String a = words[i], b = words[j];
                for (int k = Math.min(a.length(), b.length()); k > 0; k--) {
                    if (a.substring(a.length() - k).equals(b.substring(0, k))) {
                        overlap[i][j] = k;
                        break;
                    }
                }
            }
        }
        int N = 1 << n;
        String[][] dp = new String[N][n];
        for (int i = 0; i < n; i++) dp[1 << i][i] = words[i];
        for (int mask = 0; mask < N; mask++) {
            for (int last = 0; last < n; last++) {
                if ((mask & (1 << last)) == 0 || dp[mask][last] == null) continue;
                for (int nxt = 0; nxt < n; nxt++) {
                    if ((mask & (1 << nxt)) != 0) continue;
                    String cand = dp[mask][last] + words[nxt].substring(overlap[last][nxt]);
                    int nmask = mask | (1 << nxt);
                    if (dp[nmask][nxt] == null || cand.length() < dp[nmask][nxt].length())
                        dp[nmask][nxt] = cand;
                }
            }
        }
        int full = N - 1;
        String best = null;
        for (int i = 0; i < n; i++) {
            if (dp[full][i] != null && (best == null || dp[full][i].length() < best.length()))
                best = dp[full][i];
        }
        return best;
    }
}
