// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

class Solution {
    func longestPalindrome(_ word1: String, _ word2: String) -> Int {
        let s = Array(word1) + Array(word2)
        let n = s.count
        let n1 = word1.count
        var dp = [[Int]](repeating: [Int](repeating: 0, count: n), count: n)
        var ans = 0
        for i in stride(from: n - 1, through: 0, by: -1) {
            dp[i][i] = 1
            if i + 1 < n {
                for j in (i + 1)..<n {
                    if s[i] == s[j] {
                        dp[i][j] = j == i + 1 ? 2 : dp[i + 1][j - 1] + 2
                        if i < n1 && n1 <= j {
                            ans = max(ans, dp[i][j])
                        }
                    } else {
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                    }
                }
            }
        }
        return ans
    }
}
