// LeetCode 1985 - Find the Kth Largest Integer in the Array
// https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

import "sort"

func kthLargestNumber(nums []string, k int) string {
	sort.Slice(nums, func(i, j int) bool {
		if len(nums[i]) != len(nums[j]) {
			return len(nums[i]) > len(nums[j])
		}
		return nums[i] > nums[j]
	})
	return nums[k-1]
}
