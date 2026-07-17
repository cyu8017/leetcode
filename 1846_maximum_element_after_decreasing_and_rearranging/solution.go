// LeetCode 1846 - Maximum Element After Decreasing and Rearranging
// https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

import "sort"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	sort.Ints(arr)
	arr[0] = 1
	for i := 1; i < len(arr); i++ {
		if arr[i] > arr[i-1]+1 {
			arr[i] = arr[i-1] + 1
		}
	}
	maxVal := arr[0]
	for _, value := range arr {
		if value > maxVal {
			maxVal = value
		}
	}
	return maxVal
}
