// LeetCode 1168 - Optimize Water Distribution in a Village
// https://leetcode.com/problems/optimize-water-distribution-in-a-village/

import "sort"

func minCostToSupplyWater(n int, wells []int, pipes [][]int) int {
	parent := make([]int, n+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	edges := make([][]int, 0, len(wells)+len(pipes))
	for i, w := range wells {
		edges = append(edges, []int{0, i + 1, w})
	}
	edges = append(edges, pipes...)
	sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })
	ans := 0
	for _, e := range edges {
		a, b := find(e[0]), find(e[1])
		if a == b {
			continue
		}
		parent[b] = a
		ans += e[2]
	}
	return ans
}
