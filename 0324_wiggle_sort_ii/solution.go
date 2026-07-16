// LeetCode 0324 - Wiggle Sort II
// https://leetcode.com/problems/wiggle-sort-ii/

import "sort"

func wiggleSort(nums []int) {
	sortedNums := append([]int(nil), nums...)
	sort.Ints(sortedNums)
	left := (len(nums) - 1) / 2
	right := len(nums) - 1
	for index := range nums {
		if index%2 == 0 {
			nums[index] = sortedNums[left]
			left--
		} else {
			nums[index] = sortedNums[right]
			right--
		}
	}
}
