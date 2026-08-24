// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

class Solution {
    func maxCoins(_ lane1: [Int], _ lane2: [Int]) -> Int {
        let n = lane1.count
        let neg = -(1 << 60)
        var dp = Array(repeating: Array(repeating: 0, count: 2), count: 2)
        dp[0][0] = lane1[0]
        dp[1][0] = lane2[0]
        dp[0][1] = neg
        dp[1][1] = neg
        var ans = max(dp[0][0], dp[1][0])
        if n >= 2 {
            for i in 1..<n {
                var ndp = Array(repeating: Array(repeating: 0, count: 2), count: 2)
                ndp[0][0] = max(dp[0][0], 0) + lane1[i]
                ndp[1][0] = max(dp[1][0], 0) + lane2[i]
                ndp[0][1] = max(dp[0][1], dp[1][0]) + lane1[i]
                ndp[1][1] = max(dp[1][1], dp[0][0]) + lane2[i]
                if lane1[i] > ndp[0][0] { ndp[0][0] = lane1[i] }
                if lane2[i] > ndp[1][0] { ndp[1][0] = lane2[i] }
                for a in 0..<2 {
                    for b in 0..<2 {
                        dp[a][b] = ndp[a][b]
                        if dp[a][b] > ans { ans = dp[a][b] }
                    }
                }
            }
        }
        return ans
    }
}
