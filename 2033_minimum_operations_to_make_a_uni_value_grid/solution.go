// LeetCode 2033 - Minimum Operations to Make a Uni-Value Grid
// https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

import "sort"

func minOperations(grid [][]int, x int) int {
	vals := []int{}
	base := grid[0][0] % x
	for _, row := range grid {
		for _, v := range row {
			if v%x != base {
				return -1
			}
			vals = append(vals, v)
		}
	}
	sort.Ints(vals)
	median := vals[len(vals)/2]
	ans := 0
	for _, v := range vals {
		diff := v - median
		if diff < 0 {
			diff = -diff
		}
		ans += diff / x
	}
	return ans
}
