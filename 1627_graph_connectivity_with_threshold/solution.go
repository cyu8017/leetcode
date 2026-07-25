// LeetCode 1627 - Graph Connectivity With Threshold
// https://leetcode.com/problems/graph-connectivity-with-threshold/

func areConnected(n int, threshold int, queries [][]int) []bool {
	parent := make([]int, n+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for x != parent[x] {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for d := threshold + 1; d <= n; d++ {
		for x := 2 * d; x <= n; x += d {
			a, b := find(d), find(x)
			if a != b {
				parent[b] = a
			}
		}
	}
	ans := make([]bool, len(queries))
	for i, q := range queries {
		ans[i] = find(q[0]) == find(q[1])
	}
	return ans
}
