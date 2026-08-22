// LeetCode 3397 - Maximum Number of Distinct Elements After Operations
// https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

import "sort"

func maxDistinctElements(nums []int, k int) int {
	sort.Ints(nums)
	ans := 0
	prev := int(-1e18)
	for _, x := range nums {
		cur := x - k
		if cur <= prev {
			cur = prev + 1
		}
		if cur > x+k {
			continue
		}
		ans++
		prev = cur
	}
	return ans
}
