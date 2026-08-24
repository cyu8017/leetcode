// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

class Solution {
    func entry(_ i: Int, _ j: Int) -> Int { (i + 1) * (j + 1) }

    func minCost(_ m: Int, _ n: Int, _ waitCost: [[Int]]) -> Int {
        let INF = Int.max / 4
        var dp = Array(repeating: Array(repeating: INF, count: n), count: m)
        dp[0][0] = entry(0, 0)
        for i in 0..<m {
            for j in 0..<n {
                if i == 0 && j == 0 { continue }
                if i > 0 {
                    var cand = dp[i - 1][j] + entry(i, j)
                    if !(i - 1 == 0 && j == 0) { cand += waitCost[i - 1][j] }
                    dp[i][j] = min(dp[i][j], cand)
                }
                if j > 0 {
                    var cand = dp[i][j - 1] + entry(i, j)
                    if !(i == 0 && j - 1 == 0) { cand += waitCost[i][j - 1] }
                    dp[i][j] = min(dp[i][j], cand)
                }
            }
        }
        return dp[m - 1][n - 1]
    }
}
