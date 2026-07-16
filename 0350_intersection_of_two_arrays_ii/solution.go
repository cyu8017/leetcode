// LeetCode 0350 - Intersection of Two Arrays II
// https://leetcode.com/problems/intersection-of-two-arrays-ii/

func intersect(nums1 []int, nums2 []int) []int {
	counts := make(map[int]int)
	for _, num := range nums1 {
		counts[num]++
	}

	result := make([]int, 0)
	for _, num := range nums2 {
		if counts[num] > 0 {
			result = append(result, num)
			counts[num]--
		}
	}
	return result
}
