// LeetCode 3784 - Minimum Deletion Cost To Make All Characters Equal
// https://leetcode.com/problems/minimum-deletion-cost-to-make-all-characters-equal/

class Solution {
    func minCost(_ s: String, _ cost: [Int]) -> Int {
        let chars = Array(s)
        var tot = 0
        var g = [Character: Int]()
        for i in 0..<cost.count {
            tot += cost[i]
            g[chars[i], default: 0] += cost[i]
        }
        var ans = tot
        for x in g.values { ans = min(ans, tot - x) }
        return ans
    }
}
