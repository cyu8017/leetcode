// LeetCode 2500 - Delete Greatest Value in Each Row
// https://leetcode.com/problems/delete-greatest-value-in-each-row/

import "sort"

func deleteGreatestValue(grid [][]int) int {
	for i := range grid {
		sort.Ints(grid[i])
	}
	ans := 0
	n := len(grid[0])
	for c := 0; c < n; c++ {
		mx := 0
		for r := range grid {
			if grid[r][c] > mx {
				mx = grid[r][c]
			}
		}
		ans += mx
	}
	return ans
}
