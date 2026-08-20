// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/


func findShortestCycle(n int, edges [][]int) int {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	const INF = int(1e9)
	ans := INF
	for start := 0; start < n; start++ {
		dist := make([]int, n)
		parent := make([]int, n)
		for i := range dist {
			dist[i] = -1
			parent[i] = -1
		}
		q := []int{start}
		dist[start] = 0
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			for _, v := range g[u] {
				if dist[v] < 0 {
					dist[v] = dist[u] + 1
					parent[v] = u
					q = append(q, v)
				} else if parent[u] != v {
					if c := dist[u] + dist[v] + 1; c < ans {
						ans = c
					}
				}
			}
		}
	}
	if ans == INF {
		return -1
	}
	return ans
}
