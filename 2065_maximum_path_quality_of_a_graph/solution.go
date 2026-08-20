// LeetCode 2065 - Maximum Path Quality of a Graph
// https://leetcode.com/problems/maximum-path-quality-of-a-graph/

func maximalPathQuality(values []int, edges [][]int, maxTime int) int {
	n := len(values)
	g := make([][][2]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], [2]int{e[1], e[2]})
		g[e[1]] = append(g[e[1]], [2]int{e[0], e[2]})
	}
	ans := 0
	vis := make([]int, n)
	var dfs func(u, time, quality int)
	dfs = func(u, time, quality int) {
		if time > maxTime {
			return
		}
		first := vis[u] == 0
		if first {
			quality += values[u]
		}
		vis[u]++
		if u == 0 && quality > ans {
			ans = quality
		}
		for _, e := range g[u] {
			dfs(e[0], time+e[1], quality)
		}
		vis[u]--
	}
	dfs(0, 0, 0)
	return ans
}
