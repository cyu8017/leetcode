// LeetCode 3313 - Find the Last Marked Nodes in Tree
// https://leetcode.com/problems/find-the-last-marked-nodes-in-tree/

func lastMarkedNodes(edges [][]int) []int {
	n := len(edges) + 1
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	bfs := func(start int) (int, []int) {
		dist := make([]int, n)
		for i := range dist {
			dist[i] = -1
		}
		q := []int{start}
		dist[start] = 0
		far := start
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			if dist[u] > dist[far] {
				far = u
			}
			for _, v := range g[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					q = append(q, v)
				}
			}
		}
		return far, dist
	}
	u, _ := bfs(0)
	v, du := bfs(u)
	_, dv := bfs(v)
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		if du[i] >= dv[i] {
			ans[i] = u
		} else {
			ans[i] = v
		}
	}
	return ans
}
