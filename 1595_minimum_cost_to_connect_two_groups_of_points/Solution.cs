// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

using System;
using System.Collections.Generic;

public class Solution {
    public int ConnectTwoGroups(IList<IList<int>> cost) {
        int m = cost.Count, n = cost[0].Count;
        int full = 1 << n;
        int[] dp = new int[full];
        Array.Fill(dp, int.MaxValue / 2);
        dp[0] = 0;
        foreach (var row in cost) {
            int[] nxt = new int[full];
            Array.Fill(nxt, int.MaxValue / 2);
            for (int mask = 0; mask < full; mask++) {
                for (int j = 0; j < n; j++) {
                    int newMask = mask | (1 << j);
                    nxt[newMask] = Math.Min(nxt[newMask], Math.Min(dp[mask] + row[j], nxt[mask] + row[j]));
                }
            }
            dp = nxt;
        }
        int[] minimum = new int[n];
        for (int j = 0; j < n; j++) {
            minimum[j] = int.MaxValue;
            for (int i = 0; i < m; i++) minimum[j] = Math.Min(minimum[j], cost[i][j]);
        }
        int answer = int.MaxValue;
        for (int mask = 0; mask < full; mask++) {
            int extra = 0;
            for (int j = 0; j < n; j++)
                if ((mask & (1 << j)) == 0) extra += minimum[j];
            answer = Math.Min(answer, dp[mask] + extra);
        }
        return answer;
    }
}
