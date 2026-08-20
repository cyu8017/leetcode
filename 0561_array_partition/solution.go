// LeetCode 0561 - Array Partition
// https://leetcode.com/problems/array-partition/

import "sort"

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums); i += 2 {
		sum += nums[i]
	}
	return sum
}
