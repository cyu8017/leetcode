// LeetCode 0712 - Minimum ASCII Delete Sum for Two Strings
// https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

class Solution {
    func minimumDeleteSum(_ s1: String, _ s2: String) -> Int {
        let a = Array(s1), b = Array(s2)
        let m = a.count, n = b.count
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        if m >= 1 {
            for i in 1...m { dp[i][0] = dp[i - 1][0] + Int(a[i - 1].asciiValue!) }
        }
        if n >= 1 {
            for j in 1...n { dp[0][j] = dp[0][j - 1] + Int(b[j - 1].asciiValue!) }
        }
        if m >= 1 && n >= 1 {
            for i in 1...m {
                for j in 1...n {
                    if a[i - 1] == b[j - 1] {
                        dp[i][j] = dp[i - 1][j - 1]
                    } else {
                        dp[i][j] = min(dp[i - 1][j] + Int(a[i - 1].asciiValue!),
                                       dp[i][j - 1] + Int(b[j - 1].asciiValue!))
                    }
                }
            }
        }
        return dp[m][n]
    }
}
