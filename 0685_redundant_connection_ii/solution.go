// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

func findRedundantDirectedConnection(edges [][]int) []int {
	n := len(edges)
	parent := make([]int, n+1)
	var cand1, cand2 []int
	for i, e := range edges {
		u, v := e[0], e[1]
		if parent[v] == 0 {
			parent[v] = u
		} else {
			cand1 = []int{parent[v], v}
			cand2 = []int{u, v}
			edges[i] = []int{-1, -1}
			break
		}
	}
	uf := make([]int, n+1)
	for i := range uf {
		uf[i] = i
	}
	find := func(x int) int {
		for uf[x] != x {
			uf[x] = uf[uf[x]]
			x = uf[x]
		}
		return x
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		if u < 0 {
			continue
		}
		pu, pv := find(u), find(v)
		if pu == pv {
			if cand1 != nil {
				return cand1
			}
			return []int{u, v}
		}
		uf[pu] = pv
	}
	if cand2 != nil {
		return cand2
	}
	return []int{}
}
