// LeetCode 1885 - Count Pairs in Two Arrays
// https://leetcode.com/problems/count-pairs-in-two-arrays/

import "sort"

func countPairs(nums1 []int, nums2 []int) int {
	diff := make([]int, len(nums1))
	for i := range nums1 {
		diff[i] = nums1[i] - nums2[i]
	}
	sort.Ints(diff)

	answer := 0
	n := len(diff)
	for i := 0; i < n; i++ {
		target := -diff[i]
		lo := i + 1
		hi := n
		for lo < hi {
			mid := lo + (hi-lo)/2
			if diff[mid] <= target {
				lo = mid + 1
			} else {
				hi = mid
			}
		}
		answer += n - lo
	}
	return answer
}
