// LeetCode 1682 - Longest Palindromic Subsequence II
// https://leetcode.com/problems/longest-palindromic-subsequence-ii/

func longestPalindromeSubseq(s string) int {
	n := len(s)
	dp := make([][][]int, n)
	for i := 0; i < n; i++ {
		dp[i] = make([][]int, n)
		for j := 0; j < n; j++ {
			dp[i][j] = make([]int, 26)
		}
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			for c := 0; c < 26; c++ {
				v := dp[i+1][j][c]
				if dp[i][j-1][c] > v {
					v = dp[i][j-1][c]
				}
				dp[i][j][c] = v
			}
			if s[i] == s[j] {
				c := int(s[i] - 'a')
				inner := 0
				if length > 2 {
					for x := 0; x < 26; x++ {
						if x != c && dp[i+1][j-1][x] > inner {
							inner = dp[i+1][j-1][x]
						}
					}
				}
				if inner+2 > dp[i][j][c] {
					dp[i][j][c] = inner + 2
				}
			}
		}
	}
	best := 0
	for c := 0; c < 26; c++ {
		if dp[0][n-1][c] > best {
			best = dp[0][n-1][c]
		}
	}
	return best
}
