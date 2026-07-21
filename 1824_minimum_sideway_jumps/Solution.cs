// LeetCode 1824 - Minimum Sideway Jumps
// https://leetcode.com/problems/minimum-sideway-jumps/

using System;

public class Solution {
    public int MinSideJumps(int[] obstacles) {
        const int INF = 1_000_000_000;
        int[] dp = { 1, 0, 1 };

        foreach (int obs in obstacles) {
            bool[] blocked = { obs == 1, obs == 2, obs == 3 };
            int[] ndp = { INF, INF, INF };
            for (int lane = 0; lane < 3; lane++) {
                if (blocked[lane]) continue;
                for (int other = 0; other < 3; other++) {
                    if (blocked[other] || dp[other] == INF) continue;
                    ndp[lane] = Math.Min(ndp[lane], dp[other] + (lane != other ? 1 : 0));
                }
            }
            dp = ndp;
        }
        return Math.Min(dp[0], Math.Min(dp[1], dp[2]));
    }
}
