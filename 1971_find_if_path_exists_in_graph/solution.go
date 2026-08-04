// LeetCode 1971 - Find if Path Exists in Graph
// https://leetcode.com/problems/find-if-path-exists-in-graph/

func validPath(n int, edges [][]int, source int, destination int) bool {
	if source == destination {
		return true
	}
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	stack := []int{source}
	seen := make([]bool, n)
	seen[source] = true
	for len(stack) > 0 {
		u := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		if u == destination {
			return true
		}
		for _, v := range g[u] {
			if !seen[v] {
				seen[v] = true
				stack = append(stack, v)
			}
		}
	}
	return false
}
