// LeetCode 2673 - Make Costs of Paths Equal in a Binary Tree
// https://leetcode.com/problems/make-costs-of-paths-equal-in-a-binary-tree/

class Solution {
    func minIncrements(_ n: Int, _ cost: [Int]) -> Int {
        var cost = cost
        var ans = 0
        for i in stride(from: n / 2 - 1, through: 0, by: -1) {
            let l = 2 * i + 1, r = 2 * i + 2
            ans += abs(cost[l] - cost[r])
            cost[i] += max(cost[l], cost[r])
        }
        return ans
    }
}
