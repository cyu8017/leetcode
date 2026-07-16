// LeetCode 0296 - Best Meeting Point
// https://leetcode.com/problems/best-meeting-point/

import "sort"

func minTotalDistance(grid [][]int) int {
	rows := make([]int, 0)
	cols := make([]int, 0)

	for rowIndex, row := range grid {
		for colIndex, value := range row {
			if value == 1 {
				rows = append(rows, rowIndex)
				cols = append(cols, colIndex)
			}
		}
	}

	sort.Ints(cols)
	rowMedian := rows[len(rows)/2]
	colMedian := cols[len(cols)/2]

	total := 0
	for _, row := range rows {
		if row > rowMedian {
			total += row - rowMedian
		} else {
			total += rowMedian - row
		}
	}
	for _, col := range cols {
		if col > colMedian {
			total += col - colMedian
		} else {
			total += colMedian - col
		}
	}
	return total
}
