// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

export function mincostTickets(days: number[], costs: number[]): number {
    const dayset = new Set(days);
    const last = days[days.length - 1];
    const dp = new Array(last + 1).fill(0);
    for (let d = 1; d <= last; d++) {
        if (!dayset.has(d)) dp[d] = dp[d - 1];
        else {
            dp[d] = Math.min(dp[d - 1] + costs[0],
                Math.min(dp[Math.max(0, d - 7)] + costs[1], dp[Math.max(0, d - 30)] + costs[2]));
        }
    }
    return dp[last];
}
