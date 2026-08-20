// LeetCode 2192 - All Ancestors of a Node in a Directed Acyclic Graph
// https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

import "sort"

func getAncestors(n int, edges [][]int) [][]int {
	g := make([][]int, n)
	indeg := make([]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		indeg[e[1]]++
	}
	anc := make([]map[int]bool, n)
	for i := range anc {
		anc[i] = map[int]bool{}
	}
	q := []int{}
	for i := 0; i < n; i++ {
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range g[u] {
			anc[v][u] = true
			for a := range anc[u] {
				anc[v][a] = true
			}
			indeg[v]--
			if indeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	ans := make([][]int, n)
	for i := 0; i < n; i++ {
		for a := range anc[i] {
			ans[i] = append(ans[i], a)
		}
		sort.Ints(ans[i])
	}
	return ans
}
