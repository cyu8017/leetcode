// LeetCode 0568 - Maximum Vacation Days
// https://leetcode.com/problems/maximum-vacation-days/

public class Solution {
    public int MaxVacationDays(int[][] flights, int[][] days) {
        int cities = flights.Length;
        int weeks = days[0].Length;
        const int NEG = -1000000000;
        int[] dp = new int[cities];
        for (int i = 0; i < cities; ++i) dp[i] = NEG;
        dp[0] = 0;

        for (int week = 0; week < weeks; ++week) {
            int[] nxt = new int[cities];
            for (int i = 0; i < cities; ++i) nxt[i] = NEG;
            for (int city = 0; city < cities; ++city) {
                if (dp[city] == NEG) continue;
                for (int dest = 0; dest < cities; ++dest) {
                    if (dest == city || flights[city][dest] == 1) {
                        int val = dp[city] + days[dest][week];
                        if (val > nxt[dest]) nxt[dest] = val;
                    }
                }
            }
            dp = nxt;
        }
        int best = NEG;
        foreach (int v in dp) if (v > best) best = v;
        return best;
    }
}
