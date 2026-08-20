// LeetCode 3310 - Remove Methods From Project
// https://leetcode.com/problems/remove-methods-from-project/

func remainingMethods(n int, k int, invocations [][]int) []int {
	g := make([][]int, n)
	for _, e := range invocations {
		g[e[0]] = append(g[e[0]], e[1])
	}
	sus := make([]bool, n)
	var dfs func(int)
	dfs = func(u int) {
		if sus[u] {
			return
		}
		sus[u] = true
		for _, v := range g[u] {
			dfs(v)
		}
	}
	dfs(k)
	// if any non-suspicious invokes suspicious, cannot remove
	for _, e := range invocations {
		if !sus[e[0]] && sus[e[1]] {
			ans := make([]int, n)
			for i := range ans {
				ans[i] = i
			}
			return ans
		}
	}
	ans := []int{}
	for i := 0; i < n; i++ {
		if !sus[i] {
			ans = append(ans, i)
		}
	}
	return ans
}
