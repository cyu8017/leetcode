// LeetCode 1030 - Matrix Cells in Distance Order
// https://leetcode.com/problems/matrix-cells-in-distance-order/

import "sort"

func allCellsDistOrder(rows, cols, rCenter, cCenter int) [][]int {
	cells := make([][]int, 0, rows*cols)
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			cells = append(cells, []int{r, c})
		}
	}
	sort.Slice(cells, func(i, j int) bool {
		di := abs1030(cells[i][0]-rCenter) + abs1030(cells[i][1]-cCenter)
		dj := abs1030(cells[j][0]-rCenter) + abs1030(cells[j][1]-cCenter)
		return di < dj
	})
	return cells
}

func abs1030(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
