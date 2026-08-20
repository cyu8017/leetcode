// LeetCode 0802 - Find Eventual Safe States
// https://leetcode.com/problems/find-eventual-safe-states/

func eventualSafeNodes(graph [][]int) []int {
	n := len(graph)
	color := make([]int, n)
	var dfs func(int) bool
	dfs = func(node int) bool {
		if color[node] != 0 {
			return color[node] == 2
		}
		color[node] = 1
		for _, nei := range graph[node] {
			if !dfs(nei) {
				return false
			}
		}
		color[node] = 2
		return true
	}
	ans := []int{}
	for i := 0; i < n; i++ {
		if dfs(i) {
			ans = append(ans, i)
		}
	}
	return ans
}
