// LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
// https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

import "sort"

func rearrangeArray(nums []int) []int {
	sort.Ints(nums)
	n := len(nums)
	mid := (n + 1) / 2
	small, large := nums[:mid], nums[mid:]
	ans := make([]int, 0, n)
	i, j := 0, 0
	for i < len(small) || j < len(large) {
		if i < len(small) {
			ans = append(ans, small[i])
			i++
		}
		if j < len(large) {
			ans = append(ans, large[j])
			j++
		}
	}
	return ans
}
