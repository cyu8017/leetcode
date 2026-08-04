// LeetCode 1424 - Diagonal Traverse II
// https://leetcode.com/problems/diagonal-traverse-ii/

import "sort"

func findDiagonalOrder(nums [][]int) []int {
	diagonals := map[int][]int{}
	keys := []int{}
	for row, values := range nums {
		for col, value := range values {
			if _, ok := diagonals[row+col]; !ok {
				keys = append(keys, row+col)
			}
			diagonals[row+col] = append(diagonals[row+col], value)
		}
	}
	sort.Ints(keys)
	var answer []int
	for _, key := range keys {
		vals := diagonals[key]
		for i := len(vals) - 1; i >= 0; i-- {
			answer = append(answer, vals[i])
		}
	}
	return answer
}
