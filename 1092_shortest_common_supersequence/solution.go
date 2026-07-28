// LeetCode 1092 - Shortest Common Supersequence
// https://leetcode.com/problems/shortest-common-supersequence/

func shortestCommonSupersequence(str1 string, str2 string) string {
	m, n := len(str1), len(str2)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if str1[i-1] == str2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else if dp[i-1][j] >= dp[i][j-1] {
				dp[i][j] = dp[i-1][j]
			} else {
				dp[i][j] = dp[i][j-1]
			}
		}
	}
	i, j := m, n
	chars := []byte{}
	for i > 0 && j > 0 {
		if str1[i-1] == str2[j-1] {
			chars = append(chars, str1[i-1])
			i--
			j--
		} else if dp[i-1][j] >= dp[i][j-1] {
			chars = append(chars, str1[i-1])
			i--
		} else {
			chars = append(chars, str2[j-1])
			j--
		}
	}
	for i > 0 {
		chars = append(chars, str1[i-1])
		i--
	}
	for j > 0 {
		chars = append(chars, str2[j-1])
		j--
	}
	for l, r := 0, len(chars)-1; l < r; l, r = l+1, r-1 {
		chars[l], chars[r] = chars[r], chars[l]
	}
	return string(chars)
}
