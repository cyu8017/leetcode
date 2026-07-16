// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

func longestIncreasingPath(matrix [][]int) int {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return 0
	}
	rows, cols := len(matrix), len(matrix[0])
	memo := make([][]int, rows)
	for row := range memo {
		memo[row] = make([]int, cols)
	}
	directions := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	var dfs func(row int, col int) int
	dfs = func(row int, col int) int {
		if memo[row][col] != 0 {
			return memo[row][col]
		}
		best := 1
		for _, direction := range directions {
			nextRow := row + direction[0]
			nextCol := col + direction[1]
			if nextRow >= 0 && nextRow < rows &&
				nextCol >= 0 && nextCol < cols &&
				matrix[nextRow][nextCol] > matrix[row][col] {
				candidate := 1 + dfs(nextRow, nextCol)
				if candidate > best {
					best = candidate
				}
			}
		}
		memo[row][col] = best
		return best
	}

	best := 0
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if candidate := dfs(row, col); candidate > best {
				best = candidate
			}
		}
	}
	return best
}
