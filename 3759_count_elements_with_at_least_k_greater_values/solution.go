// LeetCode 3759 - Count Elements With At Least K Greater Values
// https://leetcode.com/problems/count-elements-with-at-least-k-greater-values/

import "sort"

func countElements(nums []int, k int) int {
	n := len(nums)
	if k == 0 {
		return n
	}
	sort.Ints(nums)
	ans := 0
	for i := 0; i < n-k; i++ {
		if nums[n-k] > nums[i] {
			ans++
		}
	}
	return ans
}
