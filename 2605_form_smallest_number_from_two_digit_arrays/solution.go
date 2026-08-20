// LeetCode 2605 - Form Smallest Number From Two Digit Arrays
// https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/


func minNumber(nums1 []int, nums2 []int) int {
	s1, s2 := map[int]bool{}, map[int]bool{}
	for _, x := range nums1 {
		s1[x] = true
	}
	for _, x := range nums2 {
		s2[x] = true
	}
	bestShared := 10
	for d := 1; d <= 9; d++ {
		if s1[d] && s2[d] && d < bestShared {
			bestShared = d
		}
	}
	if bestShared < 10 {
		return bestShared
	}
	m1, m2 := 10, 10
	for _, x := range nums1 {
		if x < m1 {
			m1 = x
		}
	}
	for _, x := range nums2 {
		if x < m2 {
			m2 = x
		}
	}
	if m1 < m2 {
		return m1*10 + m2
	}
	return m2*10 + m1
}
