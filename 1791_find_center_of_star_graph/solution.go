// LeetCode 1791 - Find Center of Star Graph
// https://leetcode.com/problems/find-center-of-star-graph/

func findCenter(edges [][]int) int {
	a, b := edges[0][0], edges[0][1]
	c, d := edges[1][0], edges[1][1]
	if a == c || a == d {
		return a
	}
	return b
}
