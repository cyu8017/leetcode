// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

func findMinHeightTrees(n int, edges [][]int) []int {
	if n <= 2 {
		nodes := make([]int, n)
		for node := 0; node < n; node++ {
			nodes[node] = node
		}
		return nodes
	}

	graph := make([][]int, n)
	degree := make([]int, n)
	for _, edge := range edges {
		left, right := edge[0], edge[1]
		graph[left] = append(graph[left], right)
		graph[right] = append(graph[right], left)
		degree[left]++
		degree[right]++
	}

	leaves := make([]int, 0)
	for node := 0; node < n; node++ {
		if degree[node] == 1 {
			leaves = append(leaves, node)
		}
	}

	remaining := n
	for remaining > 2 {
		remaining -= len(leaves)
		newLeaves := make([]int, 0)
		for _, leaf := range leaves {
			for _, neighbor := range graph[leaf] {
				degree[neighbor]--
				if degree[neighbor] == 1 {
					newLeaves = append(newLeaves, neighbor)
				}
			}
		}
		leaves = newLeaves
	}

	return leaves
}
