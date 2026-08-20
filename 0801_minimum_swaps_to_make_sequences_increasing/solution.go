// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

func minSwap(nums1 []int, nums2 []int) int {
	n := len(nums1)
	swap := make([]int, n)
	keep := make([]int, n)
	for i := range swap {
		swap[i], keep[i] = n, n
	}
	swap[0], keep[0] = 1, 0
	for i := 1; i < n; i++ {
		if nums1[i] > nums1[i-1] && nums2[i] > nums2[i-1] {
			keep[i] = keep[i-1]
			swap[i] = swap[i-1] + 1
		}
		if nums1[i] > nums2[i-1] && nums2[i] > nums1[i-1] {
			if swap[i-1] < keep[i] {
				keep[i] = swap[i-1]
			}
			if keep[i-1]+1 < swap[i] {
				swap[i] = keep[i-1] + 1
			}
		}
	}
	if swap[n-1] < keep[n-1] {
		return swap[n-1]
	}
	return keep[n-1]
}
