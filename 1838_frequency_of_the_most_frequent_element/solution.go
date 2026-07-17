// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

import "sort"

func maxFrequency(nums []int, k int) int {
	sort.Ints(nums)
	left := 0
	windowSum := 0
	best := 0

	for right, value := range nums {
		windowSum += value
		for value*(right-left+1)-windowSum > k {
			windowSum -= nums[left]
			left++
		}
		if right-left+1 > best {
			best = right - left + 1
		}
	}
	return best
}
