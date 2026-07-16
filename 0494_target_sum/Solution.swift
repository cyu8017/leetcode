// LeetCode 0494 - Target Sum
// https://leetcode.com/problems/target-sum/

class Solution {
    func findTargetSumWays(_ nums: [Int], _ target: Int) -> Int {
        let total = nums.reduce(0, +)
        if (total + target) % 2 != 0 || abs(target) > total {
            return 0
        }
        let need = (total + target) / 2
        var dp = Array(repeating: 0, count: need + 1)
        dp[0] = 1
        for num in nums {
            var amount = need
            while amount >= num {
                dp[amount] += dp[amount - num]
                amount -= 1
            }
        }
        return dp[need]
    }
}
