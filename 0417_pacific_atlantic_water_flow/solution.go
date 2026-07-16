// LeetCode 0417 - Pacific Atlantic Water Flow
// https://leetcode.com/problems/pacific-atlantic-water-flow/

func pacificAtlantic(heights [][]int) [][]int {
	if len(heights) == 0 || len(heights[0]) == 0 {
		return [][]int{}
	}

	rows, cols := len(heights), len(heights[0])
	pacific := make([][]bool, rows)
	atlantic := make([][]bool, rows)
	for row := 0; row < rows; row++ {
		pacific[row] = make([]bool, cols)
		atlantic[row] = make([]bool, cols)
	}

	var dfs func(row, col int, visited [][]bool, previous int)
	dfs = func(row, col int, visited [][]bool, previous int) {
		if row < 0 || row >= rows || col < 0 || col >= cols || visited[row][col] ||
			heights[row][col] < previous {
			return
		}
		visited[row][col] = true
		height := heights[row][col]
		dfs(row+1, col, visited, height)
		dfs(row-1, col, visited, height)
		dfs(row, col+1, visited, height)
		dfs(row, col-1, visited, height)
	}

	for row := 0; row < rows; row++ {
		dfs(row, 0, pacific, heights[row][0])
		dfs(row, cols-1, atlantic, heights[row][cols-1])
	}
	for col := 0; col < cols; col++ {
		dfs(0, col, pacific, heights[0][col])
		dfs(rows-1, col, atlantic, heights[rows-1][col])
	}

	result := make([][]int, 0)
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if pacific[row][col] && atlantic[row][col] {
				result = append(result, []int{row, col})
			}
		}
	}
	return result
}
