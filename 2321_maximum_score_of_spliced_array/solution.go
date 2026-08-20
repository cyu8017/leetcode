// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

func maximumsSplicedArray(nums1 []int, nums2 []int) int {
	kadane := func(a, b []int) int {
		best, cur, sum := 0, 0, 0
		for i := range a {
			sum += a[i]
			cur += b[i] - a[i]
			if cur < 0 {
				cur = 0
			}
			if cur > best {
				best = cur
			}
		}
		return sum + best
	}
	a, b := kadane(nums1, nums2), kadane(nums2, nums1)
	if a > b {
		return a
	}
	return b
}
