// LeetCode 0486 - Predict the Winner
// https://leetcode.com/problems/predict-the-winner/

class Solution {
    func predictTheWinner(_ nums: [Int]) -> Bool {
        let n = nums.count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n {
            dp[i][i] = nums[i]
        }
        if n >= 2 {
            for length in 2...n {
                for left in 0...(n - length) {
                    let right = left + length - 1
                    dp[left][right] = max(
                        nums[left] - dp[left + 1][right],
                        nums[right] - dp[left][right - 1]
                    )
                }
            }
        }
        return dp[0][n - 1] >= 0
    }
}
