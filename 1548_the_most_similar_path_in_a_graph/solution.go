// LeetCode 1548 - The Most Similar Path in a Graph
// https://leetcode.com/problems/the-most-similar-path-in-a-graph/

func mostSimilar(n int, roads [][]int, names []string, targetPath []string) []int {
	graph := make([][]int, n)
	for _, e := range roads {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	type state struct {
		cost int
		path []int
	}
	better := func(a, b state) bool {
		if a.cost != b.cost {
			return a.cost < b.cost
		}
		for i := 0; i < len(a.path) && i < len(b.path); i++ {
			if a.path[i] != b.path[i] {
				return a.path[i] < b.path[i]
			}
		}
		return len(a.path) < len(b.path)
	}
	dp := make([]state, n)
	for node := 0; node < n; node++ {
		cost := 0
		if names[node] != targetPath[0] {
			cost = 1
		}
		dp[node] = state{cost, []int{node}}
	}
	for i := 1; i < len(targetPath); i++ {
		next := make([]state, n)
		for node := 0; node < n; node++ {
			best := state{int(1e9), nil}
			for _, previous := range graph[node] {
				if better(dp[previous], best) {
					best = dp[previous]
				}
			}
			cost := best.cost
			if names[node] != targetPath[i] {
				cost++
			}
			path := append(append([]int{}, best.path...), node)
			next[node] = state{cost, path}
		}
		dp = next
	}
	best := dp[0]
	for _, s := range dp[1:] {
		if better(s, best) {
			best = s
		}
	}
	return best.path
}
