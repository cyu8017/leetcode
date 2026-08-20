// LeetCode 2294 - Partition Array Such That Maximum Difference Is K
// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k/

import "sort"

func partitionArray(nums []int, k int) int {
	sort.Ints(nums)
	ans := 1
	start := nums[0]
	for i := 1; i < len(nums); i++ {
		if nums[i]-start > k {
			ans++
			start = nums[i]
		}
	}
	return ans
}
