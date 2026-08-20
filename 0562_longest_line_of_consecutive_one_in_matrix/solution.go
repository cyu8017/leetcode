// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

func longestLine(mat [][]int) int {
	if len(mat) == 0 || len(mat[0]) == 0 {
		return 0
	}
	rows, cols := len(mat), len(mat[0])
	dp := make([][][4]int, rows)
	for r := range dp {
		dp[r] = make([][4]int, cols)
	}
	best := 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if mat[r][c] == 0 {
				continue
			}
			dp[r][c][0] = 1
			if c > 0 {
				dp[r][c][0] += dp[r][c-1][0]
			}
			dp[r][c][1] = 1
			if r > 0 {
				dp[r][c][1] += dp[r-1][c][1]
			}
			dp[r][c][2] = 1
			if r > 0 && c > 0 {
				dp[r][c][2] += dp[r-1][c-1][2]
			}
			dp[r][c][3] = 1
			if r > 0 && c+1 < cols {
				dp[r][c][3] += dp[r-1][c+1][3]
			}
			for _, v := range dp[r][c] {
				if v > best {
					best = v
				}
			}
		}
	}
	return best
}
