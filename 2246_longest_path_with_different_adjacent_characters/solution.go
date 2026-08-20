// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

func longestPath(parent []int, s string) int {
	n := len(parent)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[parent[i]] = append(g[parent[i]], i)
	}
	ans := 1
	var dfs func(int) int
	dfs = func(u int) int {
		best1, best2 := 0, 0
		for _, v := range g[u] {
			lenV := dfs(v)
			if s[v] == s[u] {
				continue
			}
			if lenV > best1 {
				best2 = best1
				best1 = lenV
			} else if lenV > best2 {
				best2 = lenV
			}
		}
		if 1+best1+best2 > ans {
			ans = 1 + best1 + best2
		}
		return 1 + best1
	}
	dfs(0)
	return ans
}
