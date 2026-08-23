// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

class Solution {
    public int maxVacationDays(int[][] flights, int[][] days) {
        int cities = flights.length;
        int weeks = days[0].length;
        final int NEG = -1000000000;

        int[] dp = new int[cities];
        for (int i = 0; i < cities; ++i) {
            dp[i] = NEG;
        }
        dp[0] = 0;

        for (int week = 0; week < weeks; ++week) {
            int[] nxt = new int[cities];
            for (int i = 0; i < cities; ++i) {
                nxt[i] = NEG;
            }
            for (int city = 0; city < cities; ++city) {
                if (dp[city] == NEG) {
                    continue;
                }
                for (int dest = 0; dest < cities; ++dest) {
                    if (dest == city || flights[city][dest] == 1) {
                        nxt[dest] = Math.max(nxt[dest], dp[city] + days[dest][week]);
                    }
                }
            }
            dp = nxt;
        }

        int best = NEG;
        for (int v : dp) {
            best = Math.max(best, v);
        }
        return best;
    }
}
