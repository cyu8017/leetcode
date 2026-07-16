// LeetCode 0456 - 132 Pattern
// https://leetcode.com/problems/132-pattern/

import "math"

func find132pattern(nums []int) bool {
	stack := make([]int, 0)
	third := math.MinInt

	for index := len(nums) - 1; index >= 0; index-- {
		if nums[index] < third {
			return true
		}
		for len(stack) > 0 && nums[index] > stack[len(stack)-1] {
			third = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, nums[index])
	}
	return false
}
