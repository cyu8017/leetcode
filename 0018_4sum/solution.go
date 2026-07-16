// LeetCode 0018 - 4Sum
// https://leetcode.com/problems/4sum/

import "sort"

func fourSum(nums []int, target int) [][]int {
	sort.Ints(nums)
	result := make([][]int, 0)

	for i := 0; i < len(nums)-3; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}

		for j := i + 1; j < len(nums)-2; j++ {
			if j > i+1 && nums[j] == nums[j-1] {
				continue
			}

			left := j + 1
			right := len(nums) - 1
			for left < right {
				total := nums[i] + nums[j] + nums[left] + nums[right]
				if total == target {
					result = append(result, []int{nums[i], nums[j], nums[left], nums[right]})
					for left < right && nums[left] == nums[left+1] {
						left++
					}
					for left < right && nums[right] == nums[right-1] {
						right--
					}
					left++
					right--
				} else if total < target {
					left++
				} else {
					right--
				}
			}
		}
	}

	return result
}
