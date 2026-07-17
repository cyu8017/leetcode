// LeetCode 1798 - Maximum Number of Consecutive Values You Can Make
// https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/

import "sort"

func getMaximumConsecutive(coins []int) int {
	sort.Ints(coins)
	reach := 0
	for _, coin := range coins {
		if coin > reach+1 {
			break
		}
		reach += coin
	}
	return reach + 1
}
