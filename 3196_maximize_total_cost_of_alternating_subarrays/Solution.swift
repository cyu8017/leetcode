// LeetCode 3196 - Maximize Total Cost of Alternating Subarrays
// https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

class Solution {
    private let NEG = Int.min / 4
    private var nums: [Int] = []
    private var memo: [[Int]] = []
    private var n = 0

    func maximumTotalCost(_ nums: [Int]) -> Int {
        self.nums = nums
        n = nums.count
        memo = Array(repeating: [NEG, NEG], count: n)
        return dfs(0, 0)
    }

    private func dfs(_ i: Int, _ j: Int) -> Int {
        if i >= n { return 0 }
        if memo[i][j] != NEG { return memo[i][j] }
        var res = nums[i] + dfs(i + 1, 1)
        if j > 0 { res = max(res, -nums[i] + dfs(i + 1, 0)) }
        memo[i][j] = res
        return res
    }
}
