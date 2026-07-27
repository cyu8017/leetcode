// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

class Solution {
    func longestPalindromeSubseq(_ s: String) -> Int {
        let chars = Array(s.utf8)
        let n = chars.count
        var dp = Array(repeating: Array(repeating: Array(repeating: 0, count: 26), count: n), count: n)
        for length in 2...n {
            for i in 0...(n - length) {
                let j = i + length - 1
                for c in 0..<26 {
                    dp[i][j][c] = max(dp[i + 1][j][c], dp[i][j - 1][c])
                }
                if chars[i] == chars[j] {
                    let c = Int(chars[i]) - 97
                    var inner = 0
                    if length > 2 {
                        for x in 0..<26 where x != c {
                            inner = max(inner, dp[i + 1][j - 1][x])
                        }
                    }
                    dp[i][j][c] = max(dp[i][j][c], inner + 2)
                }
            }
        }
        return dp[0][n - 1].max() ?? 0
    }
}
