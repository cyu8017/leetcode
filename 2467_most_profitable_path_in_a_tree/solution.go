// LeetCode 2467 - Most Profitable Path in a Tree
// https://leetcode.com/problems/most-profitable-path-in-a-tree/

func mostProfitablePath(edges [][]int, bob int, amount []int) int {
	n := len(amount)
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	bobTime := make([]int, n)
	for i := range bobTime {
		bobTime[i] = n
	}
	var findBob func(u, p, t int) bool
	findBob = func(u, p, t int) bool {
		if u == 0 {
			bobTime[u] = t
			return true
		}
		for _, v := range g[u] {
			if v == p {
				continue
			}
			if findBob(v, u, t+1) {
				bobTime[u] = t
				return true
			}
		}
		return false
	}
	findBob(bob, -1, 0)
	ans := -1 << 60
	var dfs func(u, p, t, income int)
	dfs = func(u, p, t, income int) {
		cur := amount[u]
		if t > bobTime[u] {
			cur = 0
		} else if t == bobTime[u] {
			cur /= 2
		}
		income += cur
		isLeaf := true
		for _, v := range g[u] {
			if v != p {
				isLeaf = false
				dfs(v, u, t+1, income)
			}
		}
		if isLeaf && income > ans {
			ans = income
		}
	}
	dfs(0, -1, 0, 0)
	return ans
}
