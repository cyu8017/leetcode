// LeetCode 0228 - Summary Ranges
// https://leetcode.com/problems/summary-ranges/

import "strconv"

func summaryRanges(nums []int) []string {
	result := []string{}
	index := 0

	for index < len(nums) {
		start := nums[index]
		for index+1 < len(nums) && nums[index+1] == nums[index]+1 {
			index++
		}
		if start == nums[index] {
			result = append(result, strconv.Itoa(start))
		} else {
			result = append(result, strconv.Itoa(start)+"->"+strconv.Itoa(nums[index]))
		}
		index++
	}

	return result
}
