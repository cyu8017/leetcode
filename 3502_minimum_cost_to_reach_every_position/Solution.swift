// LeetCode 3502 - Minimum Cost to Reach Every Position
// https://leetcode.com/problems/minimum-cost-to-reach-every-position/

class Solution {
    func minCosts(_ cost: [Int]) -> [Int] {
        var ans = Array(repeating: 0, count: cost.count)
        var mi = cost[0]
        for i in 0..<cost.count {
            mi = min(mi, cost[i])
            ans[i] = mi
        }
        return ans
    }
}
