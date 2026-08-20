// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

import "sort"

func placedCoins(edges [][]int, cost []int) []int64 {
	n := len(cost)
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	ans := make([]int64, n)
	var dfs func(int, int) []int
	dfs = func(u, p int) []int {
		vals := []int{cost[u]}
		for _, v := range g[u] {
			if v == p {
				continue
			}
			vals = append(vals, dfs(v, u)...)
		}
		sort.Ints(vals)
		if len(vals) < 3 {
			ans[u] = 1
		} else {
			m := len(vals)
			cand1 := int64(vals[m-1]) * int64(vals[m-2]) * int64(vals[m-3])
			cand2 := int64(vals[0]) * int64(vals[1]) * int64(vals[m-1])
			best := cand1
			if cand2 > best {
				best = cand2
			}
			if best < 0 {
				best = 0
			}
			ans[u] = best
		}
		if len(vals) <= 5 {
			return vals
		}
		return append(append([]int{}, vals[:2]...), vals[len(vals)-3:]...)
	}
	dfs(0, -1)
	return ans
}
