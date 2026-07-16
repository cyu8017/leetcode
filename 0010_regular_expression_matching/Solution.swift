// LeetCode 0010 - Regular Expression Matching
// https://leetcode.com/problems/regular-expression-matching/

class Solution {
    func isMatch(_ s: String, _ p: String) -> Bool {
        let sChars = Array(s)
        let pChars = Array(p)
        let m = sChars.count
        let n = pChars.count
        var dp = Array(repeating: Array(repeating: false, count: n + 1), count: m + 1)
        dp[0][0] = true

        if n >= 2 {
            for j in stride(from: 2, through: n, by: 1) {
                if pChars[j - 1] == "*" {
                    dp[0][j] = dp[0][j - 2]
                }
            }
        }

        for i in 1...m {
            for j in 1...n {
                if pChars[j - 1] == "*" {
                    dp[i][j] = dp[i][j - 2]
                    if pChars[j - 2] == "." || pChars[j - 2] == sChars[i - 1] {
                        dp[i][j] = dp[i][j] || dp[i - 1][j]
                    }
                } else if pChars[j - 1] == "." || pChars[j - 1] == sChars[i - 1] {
                    dp[i][j] = dp[i - 1][j - 1]
                }
            }
        }

        return dp[m][n]
    }
}
