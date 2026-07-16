// LeetCode 0349 - Intersection of Two Arrays
// https://leetcode.com/problems/intersection-of-two-arrays/

func intersection(nums1 []int, nums2 []int) []int {
	set1 := make(map[int]bool)
	set2 := make(map[int]bool)
	for _, num := range nums1 {
		set1[num] = true
	}
	for _, num := range nums2 {
		set2[num] = true
	}

	result := make([]int, 0)
	for value := range set1 {
		if set2[value] {
			result = append(result, value)
		}
	}
	return result
}
