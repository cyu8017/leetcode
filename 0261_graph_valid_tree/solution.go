// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

func validTree(n int, edges [][]int) bool {
	if len(edges) != n-1 {
		return false
	}
	parent := make([]int, n)
	for i := range parent {
		parent[i] = i
	}

	var find func(node int) int
	find = func(node int) int {
		if parent[node] != node {
			parent[node] = find(parent[node])
		}
		return parent[node]
	}

	for _, edge := range edges {
		rootLeft := find(edge[0])
		rootRight := find(edge[1])
		if rootLeft == rootRight {
			return false
		}
		parent[rootLeft] = rootRight
	}
	return true
}
