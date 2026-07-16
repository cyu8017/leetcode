// LeetCode 0516 - Longest Palindromic Subsequence
// https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution {
    func longestPalindromeSubseq(_ s: String) -> Int {
        let chars = Array(s)
        let length = chars.count
        var dp = Array(repeating: Array(repeating: 0, count: length), count: length)

        for index in stride(from: length - 1, through: 0, by: -1) {
            dp[index][index] = 1
            for end in (index + 1)..<length {
                if chars[index] == chars[end] {
                    dp[index][end] = dp[index + 1][end - 1] + 2
                } else {
                    dp[index][end] = max(dp[index + 1][end], dp[index][end - 1])
                }
            }
        }

        return dp[0][length - 1]
    }
}
