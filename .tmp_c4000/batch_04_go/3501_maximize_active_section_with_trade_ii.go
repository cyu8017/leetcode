// LeetCode 3501 - Maximize Active Section with Trade II
// https://leetcode.com/problems/maximize-active-section-with-trade-ii/

func maxActiveSectionsAfterTrade(s string, queries [][]int) []int {
	ones := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		}
	}
	ans := make([]int, len(queries))
	for i := range queries {
		ans[i] = ones
	}
	return ans
}
