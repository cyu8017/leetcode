// LeetCode 2925 - Maximum Score After Applying Operations on a Tree
// https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/

func maximumScoreAfterOperations(edges [][]int, values []int) int64 {
	n := len(values)
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	var total int64
	for _, v := range values {
		total += int64(v)
	}
	var dfs func(int, int) int64
	dfs = func(u, p int) int64 {
		var sumKids int64
		isLeaf := true
		for _, v := range g[u] {
			if v == p {
				continue
			}
			isLeaf = false
			sumKids += dfs(v, u)
		}
		if isLeaf {
			return int64(values[u])
		}
		if int64(values[u]) < sumKids {
			return int64(values[u])
		}
		return sumKids
	}
	return total - dfs(0, -1)
}
