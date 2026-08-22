// LeetCode 3938 - Maximum Path Intersection Sum in a Grid
// https://leetcode.com/problems/maximum-path-intersection-sum-in-a-grid/

func maxPathSum(grid [][]int) int {
	rows, cols := len(grid), len(grid[0])
	const negativeInfinity = -int(^uint(0)>>1) - 1
	answer := negativeInfinity

	checkLine := func(length int, value func(int) int) {
		bestEnding := value(0) + value(1)
		if bestEnding > answer {
			answer = bestEnding
		}
		for i := 2; i < length; i++ {
			if value(i-1)+value(i) > bestEnding+value(i) {
				bestEnding = value(i-1) + value(i)
			} else {
				bestEnding += value(i)
			}
			if bestEnding > answer {
				answer = bestEnding
			}
		}
	}

	for row := 0; row < rows; row++ {
		checkLine(cols, func(col int) int { return grid[row][col] })
	}
	for col := 0; col < cols; col++ {
		checkLine(rows, func(row int) int { return grid[row][col] })
	}
	for row := 1; row+1 < rows; row++ {
		for col := 1; col+1 < cols; col++ {
			if grid[row][col] > answer {
				answer = grid[row][col]
			}
		}
	}
	return answer
}