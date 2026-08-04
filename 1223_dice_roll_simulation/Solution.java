// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

class Solution {
    public int dieSimulator(int n, int[] rollMax) {
        int mod = 1_000_000_007;
        int[][] dp = new int[6][];
        for (int j = 0; j < 6; j++) {
            dp[j] = new int[rollMax[j] + 1];
            dp[j][1] = 1;
        }
        for (int t = 1; t < n; t++) {
            int[] totals = new int[6];
            for (int j = 0; j < 6; j++) {
                for (int run = 1; run < dp[j].length; run++) {
                    totals[j] = (totals[j] + dp[j][run]) % mod;
                }
            }
            int[][] nxt = new int[6][];
            for (int j = 0; j < 6; j++) {
                nxt[j] = new int[dp[j].length];
                int sumOthers = 0;
                for (int k = 0; k < 6; k++) {
                    if (k != j) sumOthers = (sumOthers + totals[k]) % mod;
                }
                nxt[j][1] = sumOthers;
                for (int run = 2; run < dp[j].length; run++) {
                    nxt[j][run] = dp[j][run - 1];
                }
            }
            dp = nxt;
        }
        int ans = 0;
        for (int j = 0; j < 6; j++) {
            for (int run = 1; run < dp[j].length; run++) {
                ans = (ans + dp[j][run]) % mod;
            }
        }
        return ans;
    }
}

