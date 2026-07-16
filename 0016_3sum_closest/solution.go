// LeetCode 0016 - 3Sum Closest
// https://leetcode.com/problems/3sum-closest/

import "sort"

func absDiff(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closest := nums[0] + nums[1] + nums[2]

	for i := 0; i < len(nums)-2; i++ {
		left := i + 1
		right := len(nums) - 1
		for left < right {
			total := nums[i] + nums[left] + nums[right]
			if absDiff(total, target) < absDiff(closest, target) {
				closest = total
			}
			if total < target {
				left++
			} else if total > target {
				right--
			} else {
				return total
			}
		}
	}

	return closest
}
