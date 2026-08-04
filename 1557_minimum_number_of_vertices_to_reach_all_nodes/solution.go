// LeetCode 1557 - Minimum Number of Vertices to Reach All Nodes
// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

func findSmallestSetOfVertices(n int, edges [][]int) []int {
	incoming := make([]bool, n)
	for _, e := range edges {
		incoming[e[1]] = true
	}
	ans := []int{}
	for v := 0; v < n; v++ {
		if !incoming[v] {
			ans = append(ans, v)
		}
	}
	return ans
}
