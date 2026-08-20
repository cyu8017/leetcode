// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

func maximumPoints(edges [][]int, coins []int, k int) int {
	n := len(coins)
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	memo := map[[2]int]int{}
	var dfs func(int, int, int) int
	dfs = func(u, p, shifts int) int {
		if shifts > 14 {
			shifts = 14
		}
		key := [2]int{u, shifts}
		if v, ok := memo[key]; ok {
			return v
		}
		c := coins[u] >> shifts
		opt1 := c - k
		opt2 := c / 2
		for _, v := range g[u] {
			if v == p {
				continue
			}
			opt1 += dfs(v, u, shifts)
			opt2 += dfs(v, u, shifts+1)
		}
		best := opt1
		if opt2 > best {
			best = opt2
		}
		memo[key] = best
		return best
	}
	return dfs(0, -1, 0)
}
