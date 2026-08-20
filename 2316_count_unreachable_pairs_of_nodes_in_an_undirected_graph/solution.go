// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

func countPairs(n int, edges [][]int) int64 {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	vis := make([]bool, n)
	var dfs func(int) int
	dfs = func(u int) int {
		vis[u] = true
		size := 1
		for _, v := range g[u] {
			if !vis[v] {
				size += dfs(v)
			}
		}
		return size
	}
	var ans, seen int64
	for i := 0; i < n; i++ {
		if !vis[i] {
			sz := int64(dfs(i))
			ans += sz * seen
			seen += sz
		}
	}
	return ans
}
