// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

func minimumWeight(edges [][]int, queries [][]int) []int {
	n := len(edges) + 1
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], edge{v, w})
		g[v] = append(g[v], edge{u, w})
	}
	const LOG = 17
	parent := make([][]int, LOG)
	for i := 0; i < LOG; i++ {
		parent[i] = make([]int, n)
		for j := range parent[i] {
			parent[i][j] = -1
		}
	}
	depth := make([]int, n)
	dist := make([]int, n)
	var dfs func(u, p int)
	dfs = func(u, p int) {
		parent[0][u] = p
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			depth[e.to] = depth[u] + 1
			dist[e.to] = dist[u] + e.w
			dfs(e.to, u)
		}
	}
	dfs(0, -1)
	for k := 1; k < LOG; k++ {
		for v := 0; v < n; v++ {
			if parent[k-1][v] != -1 {
				parent[k][v] = parent[k-1][parent[k-1][v]]
			}
		}
	}
	lca := func(u, v int) int {
		if depth[u] < depth[v] {
			u, v = v, u
		}
		for k := LOG - 1; k >= 0; k-- {
			if parent[k][u] != -1 && depth[parent[k][u]] >= depth[v] {
				u = parent[k][u]
			}
		}
		if u == v {
			return u
		}
		for k := LOG - 1; k >= 0; k-- {
			if parent[k][u] != -1 && parent[k][u] != parent[k][v] {
				u = parent[k][u]
				v = parent[k][v]
			}
		}
		return parent[0][u]
	}
	path := func(u, v int) int {
		a := lca(u, v)
		return dist[u] + dist[v] - 2*dist[a]
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		a, b, c := q[0], q[1], q[2]
		ans[i] = (path(a, b) + path(b, c) + path(a, c)) / 2
	}
	return ans
}
