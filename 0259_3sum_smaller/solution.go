// LeetCode 0259 - 3Sum Smaller
// https://leetcode.com/problems/3sum-smaller/

import "sort"

func threeSumSmaller(nums []int, target int) int {
	sort.Ints(nums)
	count := 0
	for index := 0; index < len(nums)-2; index++ {
		left := index + 1
		right := len(nums) - 1
		for left < right {
			total := nums[index] + nums[left] + nums[right]
			if total < target {
				count += right - left
				left++
			} else {
				right--
			}
		}
	}
	return count
}
