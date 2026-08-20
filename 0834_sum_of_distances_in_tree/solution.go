// LeetCode 0834 - Sum of Distances in Tree
// https://leetcode.com/problems/sum-of-distances-in-tree/

func sumOfDistancesInTree(n int, edges [][]int) []int {
	graph := make([][]int, n)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], e[1])
		graph[e[1]] = append(graph[e[1]], e[0])
	}
	count := make([]int, n)
	ans := make([]int, n)
	for i := range count {
		count[i] = 1
	}
	var post func(int, int)
	post = func(node, parent int) {
		for _, child := range graph[node] {
			if child == parent {
				continue
			}
			post(child, node)
			count[node] += count[child]
			ans[node] += ans[child] + count[child]
		}
	}
	var reroot func(int, int)
	reroot = func(node, parent int) {
		for _, child := range graph[node] {
			if child == parent {
				continue
			}
			ans[child] = ans[node] - count[child] + (n - count[child])
			reroot(child, node)
		}
	}
	post(0, -1)
	reroot(0, -1)
	return ans
}
