// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

import "sort"

func frequencySort(nums []int) []int {
	count := map[int]int{}
	for _, x := range nums {
		count[x]++
	}
	sort.Slice(nums, func(i, j int) bool {
		if count[nums[i]] == count[nums[j]] {
			return nums[i] > nums[j]
		}
		return count[nums[i]] < count[nums[j]]
	})
	return nums
}
