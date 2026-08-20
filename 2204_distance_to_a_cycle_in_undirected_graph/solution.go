// LeetCode 2204 - Distance to a Cycle in Undirected Graph
// https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/

func distanceToCycle(n int, edges [][]int) []int {
	g := make([][]int, n)
	deg := make([]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
		deg[e[0]]++
		deg[e[1]]++
	}
	q := []int{}
	for i := 0; i < n; i++ {
		if deg[i] == 1 {
			q = append(q, i)
		}
	}
	onCycle := make([]bool, n)
	for i := range onCycle {
		onCycle[i] = true
	}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		onCycle[u] = false
		for _, v := range g[u] {
			deg[v]--
			if deg[v] == 1 {
				q = append(q, v)
			}
		}
	}
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	qq := []int{}
	for i := 0; i < n; i++ {
		if onCycle[i] {
			ans[i] = 0
			qq = append(qq, i)
		}
	}
	for len(qq) > 0 {
		u := qq[0]
		qq = qq[1:]
		for _, v := range g[u] {
			if ans[v] == -1 {
				ans[v] = ans[u] + 1
				qq = append(qq, v)
			}
		}
	}
	return ans
}
