// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

func minOperationsQueries(n int, edges [][]int, queries [][]int) []int {
	g := make([][][2]int, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], [2]int{v, w})
		g[v] = append(g[v], [2]int{u, w})
	}
	const LOG = 15
	up := make([][]int, LOG)
	for i := range up {
		up[i] = make([]int, n)
	}
	depth := make([]int, n)
	cnt := make([][27]int, n)
	var dfs func(int, int)
	dfs = func(u, p int) {
		up[0][u] = p
		for _, e := range g[u] {
			v, w := e[0], e[1]
			if v == p {
				continue
			}
			depth[v] = depth[u] + 1
			cnt[v] = cnt[u]
			cnt[v][w]++
			dfs(v, u)
		}
	}
	dfs(0, 0)
	for j := 1; j < LOG; j++ {
		for i := 0; i < n; i++ {
			up[j][i] = up[j-1][up[j-1][i]]
		}
	}
	lca := func(a, b int) int {
		if depth[a] < depth[b] {
			a, b = b, a
		}
		diff := depth[a] - depth[b]
		for j := 0; j < LOG; j++ {
			if diff&(1<<j) != 0 {
				a = up[j][a]
			}
		}
		if a == b {
			return a
		}
		for j := LOG - 1; j >= 0; j-- {
			if up[j][a] != up[j][b] {
				a = up[j][a]
				b = up[j][b]
			}
		}
		return up[0][a]
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		a, b := q[0], q[1]
		c := lca(a, b)
		total := depth[a] + depth[b] - 2*depth[c]
		best := 0
		for w := 1; w <= 26; w++ {
			f := cnt[a][w] + cnt[b][w] - 2*cnt[c][w]
			if f > best {
				best = f
			}
		}
		ans[i] = total - best
	}
	return ans
}
