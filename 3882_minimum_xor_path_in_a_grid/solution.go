// LeetCode 3882 - Minimum XOR Path in a Grid
// https://leetcode.com/problems/minimum-xor-path-in-a-grid/

func minXor(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	dp := make([][1024]bool, cols)
	for row := 0; row < rows; row++ {
		left := [1024]bool{}
		for col := 0; col < cols; col++ {
			next := [1024]bool{}
			value := grid[row][col]
			if row == 0 && col == 0 {
				next[value] = true
			} else {
				for xor := 0; xor < 1024; xor++ {
					if dp[col][xor] || left[xor] {
						next[xor^value] = true
					}
				}
			}
			dp[col] = next
			left = next
		}
	}
	for xor, reachable := range dp[cols-1] {
		if reachable {
			return xor
		}
	}
	return -1
}