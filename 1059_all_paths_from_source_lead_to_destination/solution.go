// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

func leadsToDestination(n int, edges [][]int, source int, destination int) bool {
	graph := make([][]int, n)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
	}
	state := make([]int, n) // 0 unvisited, 1 in progress, 2 confirmed

	var dfs func(int) bool
	dfs = func(node int) bool {
		if len(graph[node]) == 0 {
			return node == destination
		}
		if state[node] == 1 {
			return false
		}
		if state[node] == 2 {
			return true
		}
		state[node] = 1
		for _, nxt := range graph[node] {
			if !dfs(nxt) {
				return false
			}
		}
		state[node] = 2
		return true
	}
	return dfs(source)
}
