// LeetCode 0945 - Minimum Increment to Make Array Unique
// https://leetcode.com/problems/minimum-increment-to-make-array-unique/

import "sort"

func minIncrementForUnique(nums []int) int {
	sort.Ints(nums)
	ans := 0
	for i := 1; i < len(nums); i++ {
		if nums[i] <= nums[i-1] {
			need := nums[i-1] + 1
			ans += need - nums[i]
			nums[i] = need
		}
	}
	return ans
}
