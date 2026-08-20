// LeetCode 2956 - Find Common Elements Between Two Arrays
// https://leetcode.com/problems/find-common-elements-between-two-arrays/

func findIntersectionValues(nums1 []int, nums2 []int) []int {
	s1, s2 := map[int]bool{}, map[int]bool{}
	for _, v := range nums1 {
		s1[v] = true
	}
	for _, v := range nums2 {
		s2[v] = true
	}
	a, b := 0, 0
	for _, v := range nums1 {
		if s2[v] {
			a++
		}
	}
	for _, v := range nums2 {
		if s1[v] {
			b++
		}
	}
	return []int{a, b}
}
