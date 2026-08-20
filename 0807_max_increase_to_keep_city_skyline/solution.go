// LeetCode 0807 - Max Increase to Keep City Skyline
// https://leetcode.com/problems/max-increase-to-keep-city-skyline/

func maxIncreaseKeepingSkyline(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	rowMax := make([]int, m)
	colMax := make([]int, n)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] > rowMax[r] {
				rowMax[r] = grid[r][c]
			}
			if grid[r][c] > colMax[c] {
				colMax[c] = grid[r][c]
			}
		}
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			limit := rowMax[r]
			if colMax[c] < limit {
				limit = colMax[c]
			}
			ans += limit - grid[r][c]
		}
	}
	return ans
}
