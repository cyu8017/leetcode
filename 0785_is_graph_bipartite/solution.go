// LeetCode 0785 - Is Graph Bipartite?
// https://leetcode.com/problems/is-graph-bipartite/

func isBipartite(graph [][]int) bool {
	color := make([]int, len(graph))
	for i := range color {
		color[i] = -1
	}
	var dfs func(int, int) bool
	dfs = func(node, c int) bool {
		color[node] = c
		for _, nei := range graph[node] {
			if color[nei] == -1 {
				if !dfs(nei, c^1) {
					return false
				}
			} else if color[nei] == c {
				return false
			}
		}
		return true
	}
	for node := 0; node < len(graph); node++ {
		if color[node] == -1 && !dfs(node, 0) {
			return false
		}
	}
	return true
}
