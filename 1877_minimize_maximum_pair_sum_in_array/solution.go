// LeetCode 1877 - Minimize Maximum Pair Sum in Array
// https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

import "sort"

func minPairSum(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	best := 0
	for i := 0; i < n/2; i++ {
		pair := nums[i] + nums[n-1-i]
		if pair > best {
			best = pair
		}
	}
	return best
}
