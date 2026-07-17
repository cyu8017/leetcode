// LeetCode 1818 - Minimum Absolute Sum Difference
// https://leetcode.com/problems/minimum-absolute-sum-difference/

import "sort"

func minAbsoluteSumDiff(nums1 []int, nums2 []int) int {
	const mod = 1_000_000_007
	sortedNums1 := append([]int(nil), nums1...)
	sort.Ints(sortedNums1)

	total := 0
	for i := range nums1 {
		diff := nums1[i] - nums2[i]
		if diff < 0 {
			diff = -diff
		}
		total += diff
	}

	bestGain := 0
	for i, target := range nums2 {
		current := nums1[i] - target
		if current < 0 {
			current = -current
		}
		idx := sort.SearchInts(sortedNums1, target)
		for _, j := range []int{idx - 1, idx} {
			if j >= 0 && j < len(sortedNums1) {
				diff := sortedNums1[j] - target
				if diff < 0 {
					diff = -diff
				}
				gain := current - diff
				if gain > bestGain {
					bestGain = gain
				}
			}
		}
	}

	return (total - bestGain) % mod
}
