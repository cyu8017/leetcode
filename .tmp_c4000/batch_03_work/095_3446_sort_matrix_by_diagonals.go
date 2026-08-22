// LeetCode 3446 - Sort Matrix by Diagonals
// https://leetcode.com/problems/sort-matrix-by-diagonals/

import "sort"

func sortMatrix(grid [][]int) [][]int {
	n := len(grid)
	diags := map[int][]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			diags[i-j] = append(diags[i-j], grid[i][j])
		}
	}
	for k, arr := range diags {
		if k >= 0 {
			sort.Sort(sort.Reverse(sort.IntSlice(arr)))
		} else {
			sort.Ints(arr)
		}
		diags[k] = arr
	}
	idx := map[int]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			k := i - j
			grid[i][j] = diags[k][idx[k]]
			idx[k]++
		}
	}
	return grid
}
