// LeetCode 1329 - Sort the Matrix Diagonally
// https://leetcode.com/problems/sort-the-matrix-diagonally/

import "sort"

func diagonalSort(mat [][]int) [][]int {
	diagonals := map[int][]int{}
	for r, row := range mat {
		for c, value := range row {
			diagonals[r-c] = append(diagonals[r-c], value)
		}
	}
	for k := range diagonals {
		sort.Sort(sort.Reverse(sort.IntSlice(diagonals[k])))
	}
	for r, row := range mat {
		for c := range row {
			vals := diagonals[r-c]
			mat[r][c] = vals[len(vals)-1]
			diagonals[r-c] = vals[:len(vals)-1]
		}
	}
	return mat
}
