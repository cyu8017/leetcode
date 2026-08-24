// LeetCode 0664 - Strange Printer
// https://leetcode.com/problems/strange-printer/

class Solution {
    func strangePrinter(_ s: String) -> Int {
        let chars = Array(s)
        let n = chars.count
        if n == 0 { return 0 }
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in stride(from: n - 1, through: 0, by: -1) {
            dp[i][i] = 1
            if i + 1 < n {
                for j in (i + 1)..<n {
                    dp[i][j] = dp[i + 1][j] + 1
                    for k in (i + 1)...j {
                        if chars[k] == chars[i] {
                            dp[i][j] = min(dp[i][j], dp[i][k - 1] + (k + 1 <= j ? dp[k + 1][j] : 0))
                        }
                    }
                }
            }
        }
        return dp[0][n - 1]
    }
}
