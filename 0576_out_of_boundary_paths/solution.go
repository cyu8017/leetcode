// LeetCode 0576 - Out of Boundary Paths
// https://leetcode.com/problems/out-of-boundary-paths/

func findPaths(m int, n int, maxMove int, startRow int, startColumn int) int {
	const mod = 1000000007
	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[startRow][startColumn] = 1
	result := 0
	dirs := [][2]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	for move := 0; move < maxMove; move++ {
		nxt := make([][]int, m)
		for i := range nxt {
			nxt[i] = make([]int, n)
		}
		for row := 0; row < m; row++ {
			for col := 0; col < n; col++ {
				ways := dp[row][col]
				if ways == 0 {
					continue
				}
				for _, d := range dirs {
					nr, nc := row+d[0], col+d[1]
					if nr >= 0 && nr < m && nc >= 0 && nc < n {
						nxt[nr][nc] = (nxt[nr][nc] + ways) % mod
					} else {
						result = (result + ways) % mod
					}
				}
			}
		}
		dp = nxt
	}
	return result
}
