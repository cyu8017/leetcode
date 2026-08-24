// LeetCode 3789 - Minimum Cost To Acquire Required Items
// https://leetcode.com/problems/minimum-cost-to-acquire-required-items/

class Solution {
    func minimumCost(_ cost1: Int, _ cost2: Int, _ costBoth: Int, _ need1: Int, _ need2: Int) -> Int {
        let a = need1 * cost1 + need2 * cost2
        let b = costBoth * max(need1, need2)
        let mn = min(need1, need2)
        let c = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        return min(a, min(b, c))
    }
}
