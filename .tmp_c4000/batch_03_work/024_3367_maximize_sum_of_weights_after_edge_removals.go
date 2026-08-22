// LeetCode 3367 - Maximize Sum of Weights After Edge Removals
// https://leetcode.com/problems/maximize-sum-of-weights-after-edge-removals/

import "sort"

func maximizeSumOfWeights(edges [][]int, k int) int64 {
	n := len(edges) + 1
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], edge{e[1], e[2]})
		g[e[1]] = append(g[e[1]], edge{e[0], e[2]})
	}
	var dfs func(u, p int) (int64, int64) // with parent edge kept / not using parent slot
	dfs = func(u, p int) (int64, int64) {
		var base int64
		gains := []int64{}
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			keep, drop := dfs(e.to, u)
			base += drop
			gain := keep + int64(e.w) - drop
			if gain > 0 {
				gains = append(gains, gain)
			}
		}
		sort.Slice(gains, func(i, j int) bool { return gains[i] > gains[j] })
		with := base
		without := base
		for i := 0; i < len(gains) && i < k-1; i++ {
			with += gains[i]
		}
		for i := 0; i < len(gains) && i < k; i++ {
			without += gains[i]
		}
		return with, without
	}
	_, ans := dfs(0, -1)
	return ans
}
