// LeetCode 3593 - Minimum Increments to Equalize Leaf Paths
// https://leetcode.com/problems/minimum-increments-to-equalize-leaf-paths/

func minIncrease(n int, edges [][]int, cost []int) int {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	ans := 0
	var dfs func(u, p int) int64
	dfs = func(u, p int) int64 {
		if len(graph[u]) == 1 && p != -1 {
			return int64(cost[u])
		}
		childVals := []int64{}
		for _, v := range graph[u] {
			if v == p {
				continue
			}
			childVals = append(childVals, dfs(v, u))
		}
		if len(childVals) == 0 {
			return int64(cost[u])
		}
		var mx int64
		for _, c := range childVals {
			if c > mx {
				mx = c
			}
		}
		for _, c := range childVals {
			if c < mx {
				ans++
			}
		}
		return mx + int64(cost[u])
	}
	dfs(0, -1)
	return ans
}
