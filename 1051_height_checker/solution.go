// LeetCode 1051 - Height Checker
// https://leetcode.com/problems/height-checker/

import "sort"

func heightChecker(heights []int) int {
	sorted := append([]int(nil), heights...)
	sort.Ints(sorted)
	ans := 0
	for i := range heights {
		if heights[i] != sorted[i] {
			ans++
		}
	}
	return ans
}
