// LeetCode 2830 - Maximize the Profit as the Salesman
// https://leetcode.com/problems/maximize-the-profit-as-the-salesman/

class Solution {
    func maximizeTheProfit(_ n: Int, _ offers: [[Int]]) -> Int {
        var byEnd = Array(repeating: [[Int]](), count: n)
        for o in offers { byEnd[o[1]].append(o) }
        var dp = Array(repeating: 0, count: n + 1)
        for end in 0..<n {
            dp[end + 1] = dp[end]
            for o in byEnd[end] {
                dp[end + 1] = max(dp[end + 1], dp[o[0]] + o[2])
            }
        }
        return dp[n]
    }
}
