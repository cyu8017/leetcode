// LeetCode 0312 - Burst Balloons
// https://leetcode.com/problems/burst-balloons/

class Solution {
    func maxCoins(_ nums: [Int]) -> Int {
        let balloons = [1] + nums + [1]
        let size = balloons.count
        var dp = Array(repeating: Array(repeating: 0, count: size), count: size)
        for length in 3...size {
            for left in 0...(size - length) {
                let right = left + length - 1
                for mid in (left + 1)..<right {
                    let coins = dp[left][mid] + dp[mid][right] +
                        balloons[left] * balloons[mid] * balloons[right]
                    dp[left][right] = max(dp[left][right], coins)
                }
            }
        }
        return dp[0][size - 1]
    }
}
