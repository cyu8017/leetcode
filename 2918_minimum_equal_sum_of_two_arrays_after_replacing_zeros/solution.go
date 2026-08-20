// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

func minSum(nums1 []int, nums2 []int) int64 {
	var s1, s2 int64
	z1, z2 := 0, 0
	for _, v := range nums1 {
		if v == 0 {
			z1++
			s1++
		} else {
			s1 += int64(v)
		}
	}
	for _, v := range nums2 {
		if v == 0 {
			z2++
			s2++
		} else {
			s2 += int64(v)
		}
	}
	if z1 == 0 && s1 < s2 {
		return -1
	}
	if z2 == 0 && s2 < s1 {
		return -1
	}
	if s1 > s2 {
		return s1
	}
	return s2
}
