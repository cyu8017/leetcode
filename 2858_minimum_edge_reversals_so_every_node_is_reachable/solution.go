// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

func minEdgeReversals(n int, edges [][]int) []int {
	g := make([][][2]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], [2]int{v, 0})
		g[v] = append(g[v], [2]int{u, 1})
	}
	ans := make([]int, n)
	var dfs1 func(int, int)
	dfs1 = func(u, p int) {
		for _, e := range g[u] {
			v, w := e[0], e[1]
			if v == p {
				continue
			}
			ans[0] += w
			dfs1(v, u)
		}
	}
	dfs1(0, -1)
	var dfs2 func(int, int)
	dfs2 = func(u, p int) {
		for _, e := range g[u] {
			v, w := e[0], e[1]
			if v == p {
				continue
			}
			if w == 0 {
				ans[v] = ans[u] + 1
			} else {
				ans[v] = ans[u] - 1
			}
			dfs2(v, u)
		}
	}
	dfs2(0, -1)
	return ans
}
