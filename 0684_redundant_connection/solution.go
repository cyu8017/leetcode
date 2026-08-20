// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

func findRedundantConnection(edges [][]int) []int {
	parent := make([]int, len(edges)+1)
	for i := range parent {
		parent[i] = i
	}
	find := func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for _, e := range edges {
		u, v := e[0], e[1]
		pu, pv := find(u), find(v)
		if pu == pv {
			return []int{u, v}
		}
		parent[pu] = pv
	}
	return []int{}
}
