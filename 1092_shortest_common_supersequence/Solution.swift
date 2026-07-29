// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

class Solution {
    func shortestCommonSupersequence(_ str1: String, _ str2: String) -> String {
        let a = Array(str1)
        let b = Array(str2)
        let m = a.count
        let n = b.count
        var dp = Array(repeating: Array(repeating: 0, count: n + 1), count: m + 1)
        for i in 1...m {
            for j in 1...n {
                if a[i - 1] == b[j - 1] {
                    dp[i][j] = dp[i - 1][j - 1] + 1
                } else {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                }
            }
        }
        var i = m
        var j = n
        var chars: [Character] = []
        while i > 0 && j > 0 {
            if a[i - 1] == b[j - 1] {
                chars.append(a[i - 1])
                i -= 1
                j -= 1
            } else if dp[i - 1][j] >= dp[i][j - 1] {
                chars.append(a[i - 1])
                i -= 1
            } else {
                chars.append(b[j - 1])
                j -= 1
            }
        }
        while i > 0 {
            chars.append(a[i - 1])
            i -= 1
        }
        while j > 0 {
            chars.append(b[j - 1])
            j -= 1
        }
        return String(chars.reversed())
    }
}
