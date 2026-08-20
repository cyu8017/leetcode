// LeetCode 2974 - Minimum Number Game
// https://leetcode.com/problems/minimum-number-game/

import "sort"

func numberGame(nums []int) []int {
	sort.Ints(nums)
	for i := 0; i+1 < len(nums); i += 2 {
		nums[i], nums[i+1] = nums[i+1], nums[i]
	}
	return nums
}
