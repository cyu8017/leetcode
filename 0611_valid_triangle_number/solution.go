// LeetCode 0611 - Valid Triangle Number
// https://leetcode.com/problems/valid-triangle-number/

import "sort"

func triangleNumber(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	count := 0
	for k := n - 1; k >= 2; k-- {
		left, right := 0, k-1
		for left < right {
			if nums[left]+nums[right] > nums[k] {
				count += right - left
				right--
			} else {
				left++
			}
		}
	}
	return count
}
