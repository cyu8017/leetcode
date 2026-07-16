// LeetCode 0265 - Paint House II
// https://leetcode.com/problems/paint-house-ii/

class Solution {
    func minCostII(_ costs: [[Int]]) -> Int {
        if costs.isEmpty {
            return 0
        }
        let colorCount = costs[0].count
        var previous = costs[0]
        for row in 1..<costs.count {
            let minCost = previous.min()!
            let minIndex = previous.firstIndex(of: minCost)!
            let secondMin = previous.enumerated()
                .filter { $0.offset != minIndex }
                .map(\.element)
                .min()!
            var current = [Int]()
            current.reserveCapacity(colorCount)
            for color in 0..<colorCount {
                let extra = color == minIndex ? secondMin : minCost
                current.append(costs[row][color] + extra)
            }
            previous = current
        }
        return previous.min()!
    }
}
