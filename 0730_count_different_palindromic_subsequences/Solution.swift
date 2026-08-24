// LeetCode 0730 - Count Different Palindromic Subsequences
// https://leetcode.com/problems/count-different-palindromic-subsequences/

class Solution {
    func countPalindromicSubsequences(_ s: String) -> Int {
        let mod = 1_000_000_007
        let chars = Array(s)
        let n = chars.count
        var dp = Array(repeating: Array(repeating: 0, count: n), count: n)
        for i in 0..<n { dp[i][i] = 1 }
        if n >= 2 {
            for length in 2...n {
                for i in 0...(n - length) {
                    let j = i + length - 1
                    if chars[i] != chars[j] {
                        dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                    } else {
                        var left = i + 1, right = j - 1
                        while left <= right && chars[left] != chars[i] { left += 1 }
                        while left <= right && chars[right] != chars[i] { right -= 1 }
                        if left > right { dp[i][j] = dp[i + 1][j - 1] * 2 + 2 }
                        else if left == right { dp[i][j] = dp[i + 1][j - 1] * 2 + 1 }
                        else { dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1] }
                    }
                    dp[i][j] = (dp[i][j] % mod + mod) % mod
                }
            }
        }
        return dp[0][n - 1]
    }
}
