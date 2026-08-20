// LeetCode 1143 - Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/

class Solution {
    func longestCommonSubsequence(_ text1: String, _ text2: String) -> Int {
        let a = Array(text1), b = Array(text2)
        let m = a.count, n = b.count
        var dp = [Int](repeating: 0, count: n + 1)
        for i in 1...m {
            var prev = 0
            for j in 1...n {
                let cur = dp[j]
                if a[i - 1] == b[j - 1] { dp[j] = prev + 1 }
                else { dp[j] = max(dp[j], dp[j - 1]) }
                prev = cur
            }
        }
        return dp[n]
    }
}
