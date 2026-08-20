// LeetCode 2538 - Difference Between Maximum and Minimum Price Sum
// https://leetcode.com/problems/difference-between-maximum-and-minimum-price-sum/

func maxOutput(n int, edges [][]int, price []int) int64 {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	var ans int64
	var dfs func(u, p int) int64
	dfs = func(u, p int) int64 {
		maxChild := int64(0)
		for _, v := range g[u] {
			if v == p {
				continue
			}
			child := dfs(v, u)
			if child > maxChild {
				maxChild = child
			}
			if child > ans {
				ans = child
			}
		}
		return int64(price[u]) + maxChild
	}
	dfs(0, -1)
	return ans
}
