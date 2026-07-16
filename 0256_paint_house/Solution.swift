// LeetCode 0256 - Paint House
// https://leetcode.com/problems/paint-house/

class Solution {
    func minCost(_ costs: [[Int]]) -> Int {
        if costs.isEmpty {
            return 0
        }
        var previous = costs[0]
        for row in 1..<costs.count {
            previous = [
                costs[row][0] + min(previous[1], previous[2]),
                costs[row][1] + min(previous[0], previous[2]),
                costs[row][2] + min(previous[0], previous[1]),
            ]
        }
        return previous.min() ?? 0
    }
}
