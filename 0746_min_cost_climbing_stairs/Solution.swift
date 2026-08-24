// LeetCode 0746 - Min Cost Climbing Stairs
// https://leetcode.com/problems/min-cost-climbing-stairs/

class Solution {
    func minCostClimbingStairs(_ cost: [Int]) -> Int {
        var a = 0, b = 0
        for i in 2...cost.count {
            let c = min(a + cost[i - 2], b + cost[i - 1])
            a = b; b = c
        }
        return b
    }
}
