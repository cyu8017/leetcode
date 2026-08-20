// LeetCode 2508 - Add Edges to Make Degrees of All Nodes Even
// https://leetcode.com/problems/add-edges-to-make-degrees-of-all-nodes-even/

func isPossible(n int, edges [][]int) bool {
	deg := make([]int, n+1)
	adj := make([]map[int]bool, n+1)
	for i := 1; i <= n; i++ {
		adj[i] = map[int]bool{}
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		deg[u]++
		deg[v]++
		adj[u][v] = true
		adj[v][u] = true
	}
	odd := []int{}
	for i := 1; i <= n; i++ {
		if deg[i]%2 == 1 {
			odd = append(odd, i)
		}
	}
	if len(odd) == 0 {
		return true
	}
	if len(odd) == 2 {
		a, b := odd[0], odd[1]
		if !adj[a][b] {
			return true
		}
		for i := 1; i <= n; i++ {
			if i != a && i != b && !adj[a][i] && !adj[b][i] {
				return true
			}
		}
		return false
	}
	if len(odd) == 4 {
		a, b, c, d := odd[0], odd[1], odd[2], odd[3]
		return (!adj[a][b] && !adj[c][d]) || (!adj[a][c] && !adj[b][d]) || (!adj[a][d] && !adj[b][c])
	}
	return false
}
