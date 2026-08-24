// LeetCode 0983 - Minimum Cost For Tickets
// https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution {
    func mincostTickets(_ days: [Int], _ costs: [Int]) -> Int {
        let dayset = Set(days)
        let last = days[days.count - 1]
        var dp = [Int](repeating: 0, count: last + 1)
        for d in 1...last {
            if !dayset.contains(d) {
                dp[d] = dp[d - 1]
            } else {
                dp[d] = min(dp[d - 1] + costs[0],
                            min(dp[max(0, d - 7)] + costs[1], dp[max(0, d - 30)] + costs[2]))
            }
        }
        return dp[last]
    }
}
