// LeetCode 2860 - Happy Students
// https://leetcode.com/problems/happy-students/

import "sort"

func countWays(nums []int) int {
	sort.Ints(nums)
	n := len(nums)
	ans := 0
	if nums[0] > 0 {
		ans++
	}
	for i := 0; i < n; i++ {
		selected := i + 1
		if selected > nums[i] && (i == n-1 || selected < nums[i+1]) {
			ans++
		}
	}
	return ans
}
