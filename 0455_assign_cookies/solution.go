// LeetCode 0455 - Assign Cookies
// https://leetcode.com/problems/assign-cookies/

import "sort"

func findContentChildren(g []int, s []int) int {
	sort.Ints(g)
	sort.Ints(s)

	child := 0
	for _, cookie := range s {
		if child < len(g) && cookie >= g[child] {
			child++
		}
	}
	return child
}
