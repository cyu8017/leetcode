// LeetCode 3590 - Kth Smallest Path XOR Sum
// https://leetcode.com/problems/kth-smallest-path-xor-sum/

import "sort"

func kthSmallest(par []int, vals []int, queries [][]int) []int {
	n := len(par)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[par[i]] = append(g[par[i]], i)
	}
	xorPath := make([]int, n)
	var dfs func(u int)
	dfs = func(u int) {
		xorPath[u] ^= vals[u]
		for _, v := range g[u] {
			xorPath[v] = xorPath[u]
			dfs(v)
		}
	}
	dfs(0)
	inT := make([]int, n)
	outT := make([]int, n)
	order := []int{}
	var dfs2 func(u int)
	dfs2 = func(u int) {
		inT[u] = len(order)
		order = append(order, xorPath[u])
		for _, v := range g[u] {
			dfs2(v)
		}
		outT[u] = len(order)
	}
	dfs2(0)
	ans := make([]int, len(queries))
	for i, q := range queries {
		u, k := q[0], q[1]
		sub := append([]int{}, order[inT[u]:outT[u]]...)
		sort.Ints(sub)
		uniq := sub[:0]
		for _, x := range sub {
			if len(uniq) == 0 || uniq[len(uniq)-1] != x {
				uniq = append(uniq, x)
			}
		}
		if k > len(uniq) {
			ans[i] = -1
		} else {
			ans[i] = uniq[k-1]
		}
	}
	return ans
}
