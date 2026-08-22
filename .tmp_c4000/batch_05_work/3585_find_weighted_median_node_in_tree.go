// LeetCode 3585 - Find Weighted Median Node in Tree
// https://leetcode.com/problems/find-weighted-median-node-in-tree/

func findMedian(n int, edges [][]int, queries [][]int) []int {
	type edge struct{ to, w int }
	g := make([][]edge, n)
	for _, e := range edges {
		u, v, w := e[0], e[1], e[2]
		g[u] = append(g[u], edge{v, w})
		g[v] = append(g[v], edge{u, w})
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		u, v := q[0], q[1]
		parent := make([]int, n)
		pw := make([]int, n)
		for i := range parent {
			parent[i] = -2
		}
		parent[u] = -1
		queue := []int{u}
		for len(queue) > 0 {
			x := queue[0]
			queue = queue[1:]
			if x == v {
				break
			}
			for _, e := range g[x] {
				if parent[e.to] == -2 {
					parent[e.to] = x
					pw[e.to] = e.w
					queue = append(queue, e.to)
				}
			}
		}
		nodes := []int{v}
		weights := []int{}
		cur := v
		for cur != u {
			weights = append(weights, pw[cur])
			cur = parent[cur]
			nodes = append(nodes, cur)
		}
		for i, j := 0, len(nodes)-1; i < j; i, j = i+1, j-1 {
			nodes[i], nodes[j] = nodes[j], nodes[i]
		}
		for i, j := 0, len(weights)-1; i < j; i, j = i+1, j-1 {
			weights[i], weights[j] = weights[j], weights[i]
		}
		total := 0
		for _, w := range weights {
			total += w
		}
		need := (total + 1) / 2
		sum := 0
		med := u
		for i, w := range weights {
			sum += w
			med = nodes[i+1]
			if sum >= need {
				break
			}
		}
		ans[qi] = med
	}
	return ans
}
