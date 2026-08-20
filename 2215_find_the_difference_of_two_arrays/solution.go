// LeetCode 2215 - Find the Difference of Two Arrays
// https://leetcode.com/problems/find-the-difference-of-two-arrays/

func findDifference(nums1 []int, nums2 []int) [][]int {
	s1, s2 := map[int]bool{}, map[int]bool{}
	for _, x := range nums1 {
		s1[x] = true
	}
	for _, x := range nums2 {
		s2[x] = true
	}
	a, b := []int{}, []int{}
	for x := range s1 {
		if !s2[x] {
			a = append(a, x)
		}
	}
	for x := range s2 {
		if !s1[x] {
			b = append(b, x)
		}
	}
	return [][]int{a, b}
}
