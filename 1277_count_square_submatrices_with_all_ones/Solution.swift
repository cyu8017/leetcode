// LeetCode 1277 - Count Square Submatrices with All Ones
// https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution {
    func countSquares(_ matrix: [[Int]]) -> Int {
        let m = matrix.count, n = matrix[0].count
        var dp = matrix
        var ans = 0
        for r in 0..<m {
            for c in 0..<n {
                if dp[r][c] == 1 && r > 0 && c > 0 {
                    dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                }
                ans += dp[r][c]
            }
        }
        return ans
    }
}
