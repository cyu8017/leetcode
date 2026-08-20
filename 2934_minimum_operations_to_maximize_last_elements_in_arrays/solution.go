// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

func minOperations(nums1 []int, nums2 []int) int {
	n := len(nums1)
	calc := func(a1, a2 []int) int {
		ops := 0
		last1, last2 := a1[n-1], a2[n-1]
		for i := 0; i < n-1; i++ {
			x, y := a1[i], a2[i]
			if x <= last1 && y <= last2 {
				continue
			}
			if y <= last1 && x <= last2 {
				ops++
				continue
			}
			return 1 << 30
		}
		return ops
	}
	ans := calc(nums1, nums2)
	nums1[n-1], nums2[n-1] = nums2[n-1], nums1[n-1]
	cand := calc(nums1, nums2) + 1
	if cand < ans {
		ans = cand
	}
	if ans >= 1<<30 {
		return -1
	}
	return ans
}
