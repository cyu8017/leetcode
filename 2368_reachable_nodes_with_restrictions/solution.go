// LeetCode 2368 - Reachable Nodes With Restrictions
// https://leetcode.com/problems/reachable-nodes-with-restrictions/

func reachableNodes(n int, edges [][]int, restricted []int) int {
	ban := map[int]bool{}
	for _, r := range restricted {
		ban[r] = true
	}
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	ans := 0
	vis := make([]bool, n)
	q := []int{0}
	vis[0] = true
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		ans++
		for _, v := range g[u] {
			if !vis[v] && !ban[v] {
				vis[v] = true
				q = append(q, v)
			}
		}
	}
	return ans
}
