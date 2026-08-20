// LeetCode 0760 - Find Anagram Mappings
// https://leetcode.com/problems/find-anagram-mappings/

func anagramMappings(nums1 []int, nums2 []int) []int {
	positions := map[int][]int{}
	for i, v := range nums2 {
		positions[v] = append(positions[v], i)
	}
	ans := make([]int, len(nums1))
	for i, v := range nums1 {
		ans[i] = positions[v][0]
		positions[v] = positions[v][1:]
	}
	return ans
}
