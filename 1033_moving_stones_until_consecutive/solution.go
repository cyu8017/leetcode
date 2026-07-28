// LeetCode 1033 - Moving Stones Until Consecutive
// https://leetcode.com/problems/moving-stones-until-consecutive/

import "sort"

func numMovesStones(a, b, c int) []int {
	arr := []int{a, b, c}
	sort.Ints(arr)
	x, y, z := arr[0], arr[1], arr[2]
	minMoves := 2
	if z-x == 2 {
		minMoves = 0
	} else if y-x <= 2 || z-y <= 2 {
		minMoves = 1
	}
	return []int{minMoves, z - x - 2}
}
