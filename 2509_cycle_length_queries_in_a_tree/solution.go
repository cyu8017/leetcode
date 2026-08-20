// LeetCode 2509 - Cycle Length Queries in a Tree
// https://leetcode.com/problems/cycle-length-queries-in-a-tree/

func cycleLengthQueries(n int, queries [][]int) []int {
	ans := make([]int, len(queries))
	for i, q := range queries {
		a, b := q[0], q[1]
		steps := 0
		for a != b {
			if a > b {
				a /= 2
			} else {
				b /= 2
			}
			steps++
		}
		ans[i] = steps + 1
	}
	return ans
}
