// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

using System;
using System.Collections.Generic;

public class Solution {
    public int MincostTickets(int[] days, int[] costs) {
        var dayset = new HashSet<int>(days);
        int last = days[days.Length - 1];
        int[] dp = new int[last + 1];
        for (int d = 1; d <= last; d++) {
            if (!dayset.Contains(d)) dp[d] = dp[d - 1];
            else {
                dp[d] = Math.Min(
                    dp[d - 1] + costs[0],
                    Math.Min(dp[Math.Max(0, d - 7)] + costs[1], dp[Math.Max(0, d - 30)] + costs[2])
                );
            }
        }
        return dp[last];
    }
}
