// LeetCode 0493 - Reverse Pairs
// https://leetcode.com/problems/reverse-pairs/

import "sort"

func reversePairs(nums []int) int {
	var mergeSort func(start, end int) int
	mergeSort = func(start, end int) int {
		if start >= end {
			return 0
		}
		mid := start + (end-start)/2
		count := mergeSort(start, mid) + mergeSort(mid+1, end)
		j := mid + 1
		for i := start; i <= mid; i++ {
			for j <= end && nums[i] > 2*nums[j] {
				j++
			}
			count += j - (mid + 1)
		}
		sort.Ints(nums[start : end+1])
		return count
	}
	return mergeSort(0, len(nums)-1)
}
