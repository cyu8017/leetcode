// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

func minTrioDegree(n int, edges [][]int) int {
	adj := make([][]bool, n)
	for i := range adj {
		adj[i] = make([]bool, n)
	}
	degree := make([]int, n)
	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		adj[u][v] = true
		adj[v][u] = true
		degree[u]++
		degree[v]++
	}
	best := int(^uint(0) >> 1)
	for _, e := range edges {
		u, v := e[0]-1, e[1]-1
		for k := 0; k < n; k++ {
			if adj[u][k] && adj[v][k] {
				total := degree[u] + degree[v] + degree[k] - 6
				if total < best {
					best = total
				}
			}
		}
	}
	if best == int(^uint(0)>>1) {
		return -1
	}
	return best
}
