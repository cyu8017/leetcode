// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

import java.util.*;

class Solution {
    public int mincostTickets(int[] days, int[] costs) {
        Set<Integer> dayset = new HashSet<>();
        for (int d : days) dayset.add(d);
        int last = days[days.length - 1];
        int[] dp = new int[last + 1];
        for (int d = 1; d <= last; d++) {
            if (!dayset.contains(d)) dp[d] = dp[d - 1];
            else {
                dp[d] = Math.min(dp[d - 1] + costs[0],
                    Math.min(dp[Math.max(0, d - 7)] + costs[1], dp[Math.max(0, d - 30)] + costs[2]));
            }
        }
        return dp[last];
    }
}
