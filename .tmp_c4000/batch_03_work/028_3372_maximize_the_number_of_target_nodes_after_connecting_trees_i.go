// LeetCode 3372 - Maximize the Number of Target Nodes After Connecting Trees I
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/

func maxTargetNodes(edges1 [][]int, edges2 [][]int, k int) []int {
	n := len(edges1) + 1
	m := len(edges2) + 1
	g1 := buildTree(n, edges1)
	g2 := buildTree(m, edges2)
	cnt1 := make([]int, n)
	for i := 0; i < n; i++ {
		cnt1[i] = countWithin(g1, i, k)
	}
	best2 := 0
	if k > 0 {
		for i := 0; i < m; i++ {
			c := countWithin(g2, i, k-1)
			if c > best2 {
				best2 = c
			}
		}
	}
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = cnt1[i] + best2
	}
	return ans
}

func buildTree(n int, edges [][]int) [][]int {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	return g
}

func countWithin(g [][]int, start, k int) int {
	if k < 0 {
		return 0
	}
	n := len(g)
	vis := make([]bool, n)
	type qn struct{ u, d int }
	q := []qn{{start, 0}}
	vis[start] = true
	cnt := 0
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		cnt++
		if cur.d == k {
			continue
		}
		for _, v := range g[cur.u] {
			if !vis[v] {
				vis[v] = true
				q = append(q, qn{v, cur.d + 1})
			}
		}
	}
	return cnt
}
