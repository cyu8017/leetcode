// LeetCode 0892 - Surface Area of 3D Shapes
// https://leetcode.com/problems/surface-area-of-3d-shapes/

func surfaceArea(grid [][]int) int {
	n := len(grid)
	area := 0
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				area += grid[i][j]*4 + 2
				if i > 0 {
					m := grid[i][j]
					if grid[i-1][j] < m {
						m = grid[i-1][j]
					}
					area -= m * 2
				}
				if j > 0 {
					m := grid[i][j]
					if grid[i][j-1] < m {
						m = grid[i][j-1]
					}
					area -= m * 2
				}
			}
		}
	}
	return area
}
