// LeetCode 2493 - Divide Nodes Into the Maximum Number of Groups
// https://leetcode.com/problems/divide-nodes-into-the-maximum-number-of-groups/

func magnificentSets(n int, edges [][]int) int {
	g := make([][]int, n+1)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	color := make([]int, n+1)
	for i := range color {
		color[i] = -1
	}
	components := [][]int{}
	for i := 1; i <= n; i++ {
		if color[i] != -1 {
			continue
		}
		comp := []int{}
		q := []int{i}
		color[i] = 0
		bipartite := true
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			comp = append(comp, u)
			for _, v := range g[u] {
				if color[v] == -1 {
					color[v] = color[u] ^ 1
					q = append(q, v)
				} else if color[v] == color[u] {
					bipartite = false
				}
			}
		}
		if !bipartite {
			return -1
		}
		components = append(components, comp)
	}
	bfsDepth := func(start int) int {
		dist := make([]int, n+1)
		for i := range dist {
			dist[i] = -1
		}
		q := []int{start}
		dist[start] = 1
		best := 1
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			if dist[u] > best {
				best = dist[u]
			}
			for _, v := range g[u] {
				if dist[v] == -1 {
					dist[v] = dist[u] + 1
					q = append(q, v)
				}
			}
		}
		return best
	}
	ans := 0
	for _, comp := range components {
		best := 0
		for _, u := range comp {
			d := bfsDepth(u)
			if d > best {
				best = d
			}
		}
		ans += best
	}
	return ans
}
