// LeetCode 1519 - Number of Nodes in the Sub-Tree With the Same Label
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

func countSubTrees(n int, edges [][]int, labels string) []int {
	graph := make([][]int, n)
	for _, e := range edges {
		a, b := e[0], e[1]
		graph[a] = append(graph[a], b)
		graph[b] = append(graph[b], a)
	}
	answer := make([]int, n)
	var dfs func(int, int) [26]int
	dfs = func(node, parent int) [26]int {
		var counts [26]int
		index := labels[node] - 'a'
		counts[index] = 1
		for _, neighbor := range graph[node] {
			if neighbor != parent {
				child := dfs(neighbor, node)
				for i := 0; i < 26; i++ {
					counts[i] += child[i]
				}
			}
		}
		answer[node] = counts[index]
		return counts
	}
	dfs(0, -1)
	return answer
}
