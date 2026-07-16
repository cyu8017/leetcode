// LeetCode 0323 - Number of Connected Components in an Undirected Graph
// https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

func countComponents(n int, edges [][]int) int {
	parent := make([]int, n)
	rank := make([]int, n)
	for node := 0; node < n; node++ {
		parent[node] = node
	}

	var find func(node int) int
	find = func(node int) int {
		if parent[node] != node {
			parent[node] = find(parent[node])
		}
		return parent[node]
	}

	components := n
	for _, edge := range edges {
		left, right := edge[0], edge[1]
		rootLeft := find(left)
		rootRight := find(right)
		if rootLeft == rootRight {
			continue
		}
		if rank[rootLeft] < rank[rootRight] {
			rootLeft, rootRight = rootRight, rootLeft
		}
		parent[rootRight] = rootLeft
		if rank[rootLeft] == rank[rootRight] {
			rank[rootLeft]++
		}
		components--
	}
	return components
}
