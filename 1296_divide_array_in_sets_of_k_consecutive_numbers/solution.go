// LeetCode 1296 - Divide Array in Sets of K Consecutive Numbers
// https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

import "sort"

func isPossibleDivide(nums []int, k int) bool {
	if len(nums)%k != 0 {
		return false
	}
	counts := map[int]int{}
	for _, x := range nums {
		counts[x]++
	}
	keys := make([]int, 0, len(counts))
	for x := range counts {
		keys = append(keys, x)
	}
	sort.Ints(keys)
	for _, start := range keys {
		amount := counts[start]
		if amount == 0 {
			continue
		}
		for value := start; value < start+k; value++ {
			if counts[value] < amount {
				return false
			}
			counts[value] -= amount
		}
	}
	return true
}
