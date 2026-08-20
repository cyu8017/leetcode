// LeetCode 2371 - Minimize Maximum Value in a Grid
// https://leetcode.com/problems/minimize-maximum-value-in-a-grid/

import "sort"

func minScore(grid [][]int) [][]int {
	m, n := len(grid), len(grid[0])
	type cell struct{ v, r, c int }
	arr := make([]cell, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			arr = append(arr, cell{grid[i][j], i, j})
		}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].v < arr[j].v })
	rowMax := make([]int, m)
	colMax := make([]int, n)
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for _, cel := range arr {
		val := rowMax[cel.r]
		if colMax[cel.c] > val {
			val = colMax[cel.c]
		}
		val++
		ans[cel.r][cel.c] = val
		rowMax[cel.r] = val
		colMax[cel.c] = val
	}
	return ans
}
