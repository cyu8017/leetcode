// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/


func rootCount(edges [][]int, guesses [][]int, k int) int {
	n := len(edges) + 1
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	guessSet := map[[2]int]bool{}
	for _, gu := range guesses {
		guessSet[[2]int{gu[0], gu[1]}] = true
	}
	var dfs1 func(u, p int) int
	dfs1 = func(u, p int) int {
		cnt := 0
		for _, v := range g[u] {
			if v == p {
				continue
			}
			if guessSet[[2]int{u, v}] {
				cnt++
			}
			cnt += dfs1(v, u)
		}
		return cnt
	}
	base := dfs1(0, -1)
	ans := 0
	var dfs2 func(u, p, cur int)
	dfs2 = func(u, p, cur int) {
		if cur >= k {
			ans++
		}
		for _, v := range g[u] {
			if v == p {
				continue
			}
			nxt := cur
			if guessSet[[2]int{u, v}] {
				nxt--
			}
			if guessSet[[2]int{v, u}] {
				nxt++
			}
			dfs2(v, u, nxt)
		}
	}
	dfs2(0, -1, base)
	return ans
}
