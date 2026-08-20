// LeetCode 3331 - Find Subtree Sizes After Changes
// https://leetcode.com/problems/find-subtree-sizes-after-changes/

func findSubtreeSizes(parent []int, s string) []int {
	n := len(parent)
	g := make([][]int, n)
	for i := 1; i < n; i++ {
		g[parent[i]] = append(g[parent[i]], i)
	}
	newParent := append([]int(nil), parent...)
	last := make([]int, 26)
	for i := range last {
		last[i] = -1
	}
	var dfs1 func(int)
	dfs1 = func(u int) {
		c := s[u] - 'a'
		prev := last[c]
		if prev != -1 {
			newParent[u] = prev
		}
		last[c] = u
		for _, v := range g[u] {
			dfs1(v)
		}
		last[c] = prev
	}
	dfs1(0)
	ng := make([][]int, n)
	for i := 1; i < n; i++ {
		ng[newParent[i]] = append(ng[newParent[i]], i)
	}
	ans := make([]int, n)
	var dfs2 func(int) int
	dfs2 = func(u int) int {
		sz := 1
		for _, v := range ng[u] {
			sz += dfs2(v)
		}
		ans[u] = sz
		return sz
	}
	dfs2(0)
	return ans
}
