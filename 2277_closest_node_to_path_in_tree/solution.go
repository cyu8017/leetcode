// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

func closestNode(n int, edges [][]int, query [][]int) []int {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	const LOG = 17
	up := make([][]int, LOG)
	for i := range up {
		up[i] = make([]int, n)
	}
	depth := make([]int, n)
	var dfs func(u, p int)
	dfs = func(u, p int) {
		up[0][u] = p
		for _, v := range g[u] {
			if v != p {
				depth[v] = depth[u] + 1
				dfs(v, u)
			}
		}
	}
	dfs(0, 0)
	for k := 1; k < LOG; k++ {
		for v := 0; v < n; v++ {
			up[k][v] = up[k-1][up[k-1][v]]
		}
	}
	lift := func(v, d int) int {
		for k := 0; k < LOG; k++ {
			if (d>>k)&1 == 1 {
				v = up[k][v]
			}
		}
		return v
	}
	lca := func(a, b int) int {
		if depth[a] < depth[b] {
			a, b = b, a
		}
		a = lift(a, depth[a]-depth[b])
		if a == b {
			return a
		}
		for k := LOG - 1; k >= 0; k-- {
			if up[k][a] != up[k][b] {
				a = up[k][a]
				b = up[k][b]
			}
		}
		return up[0][a]
	}
	dist := func(a, b int) int {
		c := lca(a, b)
		return depth[a] + depth[b] - 2*depth[c]
	}
	ans := make([]int, len(query))
	for i, q := range query {
		a, b, x := q[0], q[1], q[2]
		cands := []int{lca(a, b), lca(a, x), lca(b, x)}
		best, bestD := cands[0], dist(cands[0], x)
		for _, c := range cands[1:] {
			d := dist(c, x)
			if d < bestD {
				bestD = d
				best = c
			}
		}
		ans[i] = best
	}
	return ans
}
