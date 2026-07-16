// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

class Solution {
    func combinationSum4(_ nums: [Int], _ target: Int) -> Int {
        var dp = Array(repeating: 0, count: target + 1)
        dp[0] = 1

        for amount in 1...target {
            for num in nums where amount >= num {
                dp[amount] += dp[amount - num]
            }
        }

        return dp[target]
    }
}
