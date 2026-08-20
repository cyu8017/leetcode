// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

func assignEdgeWeights(edges [][]int, queries [][]int) []int {
	const MOD = 1_000_000_007
	const LOG = 17
	n := len(edges) + 1
	depth := make([]int, n+1)
	graph := make([][]int, n+1)
	parent := make([][]int, LOG)
	for i := 0; i < LOG; i++ {
		parent[i] = make([]int, n+1)
		for j := range parent[i] {
			parent[i][j] = -1
		}
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	var dfs func(u, p int)
	dfs = func(u, p int) {
		parent[0][u] = p
		for _, v := range graph[u] {
			if v != p {
				depth[v] = depth[u] + 1
				dfs(v, u)
			}
		}
	}
	dfs(1, -1)
	for k := 1; k < LOG; k++ {
		for v := 1; v <= n; v++ {
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
	modPow := func(exp int) int {
		base, res := 2, 1
		for exp > 0 {
			if exp&1 == 1 {
				res = res * base % MOD
			}
			base = base * base % MOD
			exp >>= 1
		}
		return res
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		u, v := q[0], q[1]
		if u == v {
			ans[i] = 0
			continue
		}
		a := lca(u, v)
		d := depth[u] + depth[v] - 2*depth[a]
		ans[i] = modPow(d - 1)
	}
	return ans
}
