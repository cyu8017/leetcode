// LeetCode 0883 - Projection Area of 3D Shapes
// https://leetcode.com/problems/projection-area-of-3d-shapes/

func projectionArea(grid [][]int) int {
	n := len(grid)
	top, front, side := 0, 0, 0
	for i := 0; i < n; i++ {
		rowMax := 0
		for j := 0; j < n; j++ {
			if grid[i][j] > 0 {
				top++
			}
			if grid[i][j] > rowMax {
				rowMax = grid[i][j]
			}
		}
		front += rowMax
	}
	for j := 0; j < n; j++ {
		colMax := 0
		for i := 0; i < n; i++ {
			if grid[i][j] > colMax {
				colMax = grid[i][j]
			}
		}
		side += colMax
	}
	return top + front + side
}
