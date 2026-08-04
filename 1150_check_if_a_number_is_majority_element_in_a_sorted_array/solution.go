// LeetCode 1150 - Check If a Number Is Majority Element in a Sorted Array
// https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/

import "sort"

func isMajorityElement(nums []int, target int) bool {
	left := sort.SearchInts(nums, target)
	right := sort.Search(len(nums), func(i int) bool { return nums[i] > target })
	return right-left > len(nums)/2
}
