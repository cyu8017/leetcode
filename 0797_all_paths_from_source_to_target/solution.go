// LeetCode 0797 - All Paths From Source to Target
// https://leetcode.com/problems/all-paths-from-source-to-target/

func allPathsSourceTarget(graph [][]int) [][]int {
	target := len(graph) - 1
	answer := [][]int{}
	var dfs func(int, []int)
	dfs = func(node int, path []int) {
		if node == target {
			cp := append([]int{}, path...)
			answer = append(answer, cp)
			return
		}
		for _, nei := range graph[node] {
			path = append(path, nei)
			dfs(nei, path)
			path = path[:len(path)-1]
		}
	}
	dfs(0, []int{0})
	return answer
}
