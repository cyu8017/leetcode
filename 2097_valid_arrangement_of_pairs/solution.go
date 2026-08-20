// LeetCode 2097 - Valid Arrangement of Pairs
// https://leetcode.com/problems/valid-arrangement-of-pairs/

func validArrangement(pairs [][]int) [][]int {
	g := map[int][]int{}
	indeg, outdeg := map[int]int{}, map[int]int{}
	for _, p := range pairs {
		u, v := p[0], p[1]
		g[u] = append(g[u], v)
		outdeg[u]++
		indeg[v]++
	}
	start := pairs[0][0]
	for u := range outdeg {
		if outdeg[u]-indeg[u] == 1 {
			start = u
			break
		}
	}
	path := []int{}
	var dfs func(int)
	dfs = func(u int) {
		for len(g[u]) > 0 {
			v := g[u][len(g[u])-1]
			g[u] = g[u][:len(g[u])-1]
			dfs(v)
		}
		path = append(path, u)
	}
	dfs(start)
	for i, j := 0, len(path)-1; i < j; i, j = i+1, j-1 {
		path[i], path[j] = path[j], path[i]
	}
	ans := make([][]int, 0, len(path)-1)
	for i := 0; i+1 < len(path); i++ {
		ans = append(ans, []int{path[i], path[i+1]})
	}
	return ans
}
