// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

class Solution {
    func probabilityOfHeads(_ prob: [Double], _ target: Int) -> Double {
        var dp = [Double](repeating: 0, count: target + 1)
        dp[0] = 1
        for p in prob {
            for k in stride(from: target, through: 0, by: -1) {
                dp[k] = (k > 0 ? dp[k - 1] * p : 0) + dp[k] * (1 - p)
            }
        }
        return dp[target]
    }
}
