// LeetCode 2360 - Longest Cycle in a Graph
// https://leetcode.com/problems/longest-cycle-in-a-graph/

func longestCycle(edges []int) int {
	n := len(edges)
	vis := make([]bool, n)
	ans := -1
	for i := 0; i < n; i++ {
		if vis[i] {
			continue
		}
		dist := map[int]int{}
		cur, step := i, 0
		for cur != -1 && !vis[cur] {
			vis[cur] = true
			dist[cur] = step
			cur = edges[cur]
			step++
		}
		if cur != -1 {
			if d, ok := dist[cur]; ok {
				cycle := step - d
				if cycle > ans {
					ans = cycle
				}
			}
		}
	}
	return ans
}
