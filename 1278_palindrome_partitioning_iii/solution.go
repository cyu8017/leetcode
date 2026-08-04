// LeetCode 1278 - Palindrome Partitioning III
// https://leetcode.com/problems/palindrome-partitioning-iii/

func palindromePartition(s string, k int) int {
	n := len(s)
	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
	}
	for length := 2; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			c := 0
			if s[i] != s[j] {
				c = 1
			}
			if length > 2 {
				c += cost[i+1][j-1]
			}
			cost[i][j] = c
		}
	}
	inf := n + 1
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[0][0] = 0
	for parts := 1; parts <= k; parts++ {
		for end := parts; end <= n; end++ {
			for start := parts - 1; start < end; start++ {
				v := dp[parts-1][start] + cost[start][end-1]
				if v < dp[parts][end] {
					dp[parts][end] = v
				}
			}
		}
	}
	return dp[k][n]
}
