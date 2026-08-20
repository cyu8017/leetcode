// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

func numberOfPaths(grid [][]int, k int) int {
	const mod = 1000000007
	m, n := len(grid), len(grid[0])
	dp := make([][][]int, m)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, k)
		}
	}
	dp[0][0][grid[0][0]%k] = 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			for r := 0; r < k; r++ {
				if dp[i][j][r] == 0 {
					continue
				}
				if i+1 < m {
					nr := (r + grid[i+1][j]) % k
					dp[i+1][j][nr] = (dp[i+1][j][nr] + dp[i][j][r]) % mod
				}
				if j+1 < n {
					nr := (r + grid[i][j+1]) % k
					dp[i][j+1][nr] = (dp[i][j+1][nr] + dp[i][j][r]) % mod
				}
			}
		}
	}
	return dp[m-1][n-1][0]
}
