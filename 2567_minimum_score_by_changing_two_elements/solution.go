// LeetCode 2567 - Minimum Score by Changing Two Elements
// https://leetcode.com/problems/minimum-score-by-changing-two-elements/


import "sort"

func minimizeSum(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	a := nums[n-1] - nums[2]
	b := nums[n-3] - nums[0]
	c := nums[n-2] - nums[1]
	ans := a
	if b < ans {
		ans = b
	}
	if c < ans {
		ans = c
	}
	return ans
}
