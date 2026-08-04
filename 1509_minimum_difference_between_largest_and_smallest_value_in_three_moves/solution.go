// LeetCode 1509 - Minimum Difference Between Largest and Smallest Value in Three Moves
// https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

import "sort"

func minDifference(nums []int) int {
	if len(nums) <= 4 {
		return 0
	}
	sort.Ints(nums)
	ans := nums[len(nums)-1] - nums[0]
	for i := 0; i < 4; i++ {
		diff := nums[len(nums)-4+i] - nums[i]
		if diff < ans {
			ans = diff
		}
	}
	return ans
}
