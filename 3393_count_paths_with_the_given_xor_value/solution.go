// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

func countPathsWithXorValue(grid [][]int, k int) int {
	const mod = 1000000007
	m, n := len(grid), len(grid[0])
	dp := make([][][]int, m)
	for i := range dp {
		dp[i] = make([][]int, n)
		for j := range dp[i] {
			dp[i][j] = make([]int, 16)
		}
	}
	dp[0][0][grid[0][0]] = 1
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			for x := 0; x < 16; x++ {
				if dp[i][j][x] == 0 {
					continue
				}
				if i+1 < m {
					nx := x ^ grid[i+1][j]
					dp[i+1][j][nx] = (dp[i+1][j][nx] + dp[i][j][x]) % mod
				}
				if j+1 < n {
					nx := x ^ grid[i][j+1]
					dp[i][j+1][nx] = (dp[i][j+1][nx] + dp[i][j][x]) % mod
				}
			}
		}
	}
	return dp[m-1][n-1][k]
}
