// LeetCode 0462 - Minimum Moves to Equal Array Elements II
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

import "sort"

func minMoves2(nums []int) int {
	sort.Ints(nums)
	median := nums[len(nums)/2]
	moves := 0
	for _, value := range nums {
		if value > median {
			moves += value - median
		} else {
			moves += median - value
		}
	}
	return moves
}
