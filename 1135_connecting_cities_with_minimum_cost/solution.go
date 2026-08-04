// LeetCode 1135 - Connecting Cities With Minimum Cost
// https://leetcode.com/problems/connecting-cities-with-minimum-cost/

import "sort"

func minimumCost(n int, connections [][]int) int {
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
	sort.Slice(connections, func(i, j int) bool {
		return connections[i][2] < connections[j][2]
	})
	ans, used := 0, 0
	for _, e := range connections {
		a, b := find(e[0]), find(e[1])
		if a == b {
			continue
		}
		parent[b] = a
		ans += e[2]
		used++
		if used == n-1 {
			return ans
		}
	}
	return -1
}
