// LeetCode 3772 - Maximum Subgraph Score in a Tree
// https://leetcode.com/problems/maximum-subgraph-score-in-a-tree/

func maxSubgraphScore(n int, edges [][]int, good []int) []int {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = -2
	}
	parent[0] = -1
	order := []int{0}
	for i := 0; i < len(order); i++ {
		u := order[i]
		for _, v := range g[u] {
			if parent[v] == -2 {
				parent[v] = u
				order = append(order, v)
			}
		}
	}
	down := make([]int, n)
	for i := n - 1; i >= 0; i-- {
		u := order[i]
		down[u] = 2*good[u] - 1
		for _, v := range g[u] {
			if parent[v] == u && down[v] > 0 {
				down[u] += down[v]
			}
		}
	}
	ans := append([]int(nil), down...)
	for _, u := range order {
		for _, v := range g[u] {
			if parent[v] == u {
				outside := ans[u]
				if down[v] > 0 {
					outside -= down[v]
				}
				ans[v] = down[v]
				if outside > 0 {
					ans[v] += outside
				}
			}
		}
	}
	return ans
}