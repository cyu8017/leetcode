// LeetCode 1771 - Maximize Palindrome Length From Subsequences
// https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/

func longestPalindrome(word1 string, word2 string) int {
    s := word1 + word2
    n := len(s)
    n1 := len(word1)
    dp := make([][]int, n)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    ans := 0
    for i := n - 1; i >= 0; i-- {
        dp[i][i] = 1
        for j := i + 1; j < n; j++ {
            if s[i] == s[j] {
                if j == i+1 {
                    dp[i][j] = 2
                } else {
                    dp[i][j] = dp[i+1][j-1] + 2
                }
                if i < n1 && n1 <= j && dp[i][j] > ans {
                    ans = dp[i][j]
                }
            } else {
                if dp[i+1][j] > dp[i][j-1] {
                    dp[i][j] = dp[i+1][j]
                } else {
                    dp[i][j] = dp[i][j-1]
                }
            }
        }
    }
    return ans
}
