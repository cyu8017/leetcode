// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

func maximalSquare(matrix [][]byte) int {
	if len(matrix) == 0 {
		return 0
	}
	rows := len(matrix)
	cols := len(matrix[0])
	dp := make([]int, cols+1)
	maxSide := 0
	prev := 0
	for row := 1; row <= rows; row++ {
		for col := 1; col <= cols; col++ {
			temp := dp[col]
			if matrix[row-1][col-1] == '1' {
				dp[col] = min(dp[col], min(dp[col-1], prev)) + 1
				if dp[col] > maxSide {
					maxSide = dp[col]
				}
			} else {
				dp[col] = 0
			}
			prev = temp
		}
	}
	return maxSide * maxSide
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
