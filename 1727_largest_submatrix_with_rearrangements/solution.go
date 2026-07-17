// LeetCode 1727 - Largest Submatrix With Rearrangements
// https://leetcode.com/problems/largest-submatrix-with-rearrangements/

import "sort"

func largestSubmatrix(matrix [][]int) int {
	m, n := len(matrix), len(matrix[0])
	heights := make([]int, n)
	best := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if matrix[r][c] == 1 {
				heights[c]++
			} else {
				heights[c] = 0
			}
		}
		sorted := make([]int, n)
		copy(sorted, heights)
		sort.Sort(sort.Reverse(sort.IntSlice(sorted)))
		for width := 1; width <= n; width++ {
			if area := width * sorted[width-1]; area > best {
				best = area
			}
		}
	}
	return best
}
