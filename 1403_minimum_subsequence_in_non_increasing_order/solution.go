// LeetCode 1403 - Minimum Subsequence in Non-Increasing Order
// https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/

import "sort"

func minSubsequence(nums []int) []int {
	sort.Sort(sort.Reverse(sort.IntSlice(nums)))
	total := 0
	for _, v := range nums {
		total += v
	}
	answer := []int{}
	chosen := 0
	for _, value := range nums {
		answer = append(answer, value)
		chosen += value
		if chosen > total-chosen {
			return answer
		}
	}
	return answer
}
