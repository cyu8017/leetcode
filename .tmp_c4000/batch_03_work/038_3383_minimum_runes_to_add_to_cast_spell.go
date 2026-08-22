// LeetCode 3383 - Minimum Runes to Add to Cast Spell
// https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/

func minRunesToAdd(n int, crystals []int, flowFrom []int, flowTo []int) int {
	g := make([][]int, n)
	rg := make([][]int, n)
	for i := range flowFrom {
		a, b := flowFrom[i], flowTo[i]
		g[a] = append(g[a], b)
		rg[b] = append(rg[b], a)
	}
	// Kosaraju SCC
	vis := make([]bool, n)
	order := []int{}
	var dfs1 func(int)
	dfs1 = func(u int) {
		vis[u] = true
		for _, v := range g[u] {
			if !vis[v] {
				dfs1(v)
			}
		}
		order = append(order, u)
	}
	for i := 0; i < n; i++ {
		if !vis[i] {
			dfs1(i)
		}
	}
	comp := make([]int, n)
	for i := range comp {
		comp[i] = -1
	}
	cid := 0
	var dfs2 func(int)
	dfs2 = func(u int) {
		comp[u] = cid
		for _, v := range rg[u] {
			if comp[v] == -1 {
				dfs2(v)
			}
		}
	}
	for i := n - 1; i >= 0; i-- {
		u := order[i]
		if comp[u] == -1 {
			dfs2(u)
			cid++
		}
	}
	hasCrystal := make([]bool, cid)
	for _, c := range crystals {
		hasCrystal[comp[c]] = true
	}
	indeg := make([]int, cid)
	for u := 0; u < n; u++ {
		for _, v := range g[u] {
			if comp[u] != comp[v] {
				indeg[comp[v]]++
			}
		}
	}
	ans := 0
	for i := 0; i < cid; i++ {
		if indeg[i] == 0 && !hasCrystal[i] {
			ans++
		}
	}
	return ans
}
