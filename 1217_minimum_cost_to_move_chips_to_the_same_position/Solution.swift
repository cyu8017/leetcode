// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

class Solution {
    func minCostToMoveChips(_ position: [Int]) -> Int {
        var even = 0, odd = 0
        for p in position {
            if p % 2 == 0 { even += 1 } else { odd += 1 }
        }
        return min(even, odd)
    }
}
