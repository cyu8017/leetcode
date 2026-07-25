// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

import "sort"

func distanceLimitedPathsExist(n int, edgeList [][]int, queries [][]int) []bool {
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}
	var find func(x int) int
	find = func(x int) int {
		for x != parent[x] {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	edges := append([][]int{}, edgeList...)
	sort.Slice(edges, func(i, j int) bool { return edges[i][2] < edges[j][2] })

	type qi struct{ limit, p, q, idx int }
	qs := make([]qi, len(queries))
	for j, q := range queries {
		qs[j] = qi{q[2], q[0], q[1], j}
	}
	sort.Slice(qs, func(i, j int) bool { return qs[i].limit < qs[j].limit })

	ans := make([]bool, len(queries))
	i := 0
	for _, qq := range qs {
		for i < len(edges) && edges[i][2] < qq.limit {
			a, b := edges[i][0], edges[i][1]
			parent[find(a)] = find(b)
			i++
		}
		ans[qq.idx] = find(qq.p) == find(qq.q)
	}
	return ans
}
