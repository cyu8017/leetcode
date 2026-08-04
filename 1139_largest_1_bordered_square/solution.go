// LeetCode 1139 - Largest 1-Bordered Square
// https://leetcode.com/problems/largest-1-bordered-square/

func largest1BorderedSquare(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	hor := make([][]int, m)
	ver := make([][]int, m)
	for i := 0; i < m; i++ {
		hor[i] = make([]int, n)
		ver[i] = make([]int, n)
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				if j > 0 {
					hor[i][j] = hor[i][j-1] + 1
				} else {
					hor[i][j] = 1
				}
				if i > 0 {
					ver[i][j] = ver[i-1][j] + 1
				} else {
					ver[i][j] = 1
				}
			}
		}
	}
	for side := min(m, n); side > 0; side-- {
		for i := side - 1; i < m; i++ {
			for j := side - 1; j < n; j++ {
				if hor[i][j] >= side && ver[i][j] >= side &&
					hor[i-side+1][j] >= side && ver[i][j-side+1] >= side {
					return side * side
				}
			}
		}
	}
	return 0
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
