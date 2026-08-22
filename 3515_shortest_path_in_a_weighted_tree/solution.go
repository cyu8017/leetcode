// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

func treeQueries(n int, edges [][]int, queries [][]int) []int {
	type edge struct{ to, w int }
	g := make([][]edge, n+1)
	weight := map[[2]int]int{}
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], edge{v, w})
		g[v] = append(g[v], edge{u, w})
		a, b := u, v
		if a > b {
			a, b = b, a
		}
		weight[[2]int{a, b}] = w
	}
	inT := make([]int, n+1)
	outT := make([]int, n+1)
	dist := make([]int, n+1)
	parent := make([]int, n+1)
	time := 0
	var dfs func(u, p int)
	dfs = func(u, p int) {
		inT[u] = time
		time++
		for _, e := range g[u] {
			if e.to == p {
				continue
			}
			parent[e.to] = u
			dist[e.to] = dist[u] + e.w
			dfs(e.to, u)
		}
		outT[u] = time - 1
	}
	dfs(1, 0)
	bit := make([]int, n+2)
	add := func(i, v int) {
		for i <= n {
			bit[i] += v
			i += i & -i
		}
	}
	rangeAdd := func(l, r, v int) {
		add(l+1, v)
		add(r+2, -v)
	}
	point := func(i int) int {
		s := 0
		i++
		for i > 0 {
			s += bit[i]
			i -= i & -i
		}
		return s
	}
	for i := 1; i <= n; i++ {
		rangeAdd(inT[i], inT[i], dist[i])
	}
	var ans []int
	for _, q := range queries {
		if q[0] == 1 {
			u, v, nw := q[1], q[2], q[3]
			a, b := u, v
			if a > b {
				a, b = b, a
			}
			ow := weight[[2]int{a, b}]
			delta := nw - ow
			weight[[2]int{a, b}] = nw
			child := v
			if parent[u] == v {
				child = u
			}
			rangeAdd(inT[child], outT[child], delta)
		} else {
			ans = append(ans, point(inT[q[1]]))
		}
	}
	return ans
}
