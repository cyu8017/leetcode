// LeetCode 0474 - Ones and Zeroes
// https://leetcode.com/problems/ones-and-zeroes/

import "strings"

func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, m+1)
	for zero := 0; zero <= m; zero++ {
		dp[zero] = make([]int, n+1)
	}
	for _, stringValue := range strs {
		zeros := strings.Count(stringValue, "0")
		ones := len(stringValue) - zeros
		for zero := m; zero >= zeros; zero-- {
			for one := n; one >= ones; one-- {
				if candidate := dp[zero-zeros][one-ones] + 1; candidate > dp[zero][one] {
					dp[zero][one] = candidate
				}
			}
		}
	}
	return dp[m][n]
}
