// LeetCode 1874 - Minimize Product Sum of Two Arrays
// https://leetcode.com/problems/minimize-product-sum-of-two-arrays/

import "sort"

func minProductSum(nums1 []int, nums2 []int) int {
	sort.Ints(nums1)
	sort.Slice(nums2, func(i, j int) bool {
		return nums2[i] > nums2[j]
	})

	total := 0
	for i := range nums1 {
		total += nums1[i] * nums2[i]
	}
	return total
}
