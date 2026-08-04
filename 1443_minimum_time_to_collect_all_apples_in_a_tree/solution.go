// LeetCode 1443 - Minimum Time to Collect All Apples in a Tree
// https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

func minTime(n int, edges [][]int, hasApple []bool) int {
	graph := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	var visit func(int, int) int
	visit = func(node, parent int) int {
		cost := 0
		for _, child := range graph[node] {
			if child != parent {
				childCost := visit(child, node)
				if childCost > 0 || hasApple[child] {
					cost += childCost + 2
				}
			}
		}
		return cost
	}
	return visit(0, -1)
}
