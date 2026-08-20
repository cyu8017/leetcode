// LeetCode 3373 - Maximize the Number of Target Nodes After Connecting Trees II
// https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/

func maxTargetNodes(edges1 [][]int, edges2 [][]int) []int {
	n := len(edges1) + 1
	m := len(edges2) + 1
	g1 := buildTree3373(n, edges1)
	g2 := buildTree3373(m, edges2)
	color1 := make([]int, n)
	color2 := make([]int, m)
	c1 := bipartiteCount(g1, color1)
	c2 := bipartiteCount(g2, color2)
	best2 := c2[0]
	if c2[1] > best2 {
		best2 = c2[1]
	}
	ans := make([]int, n)
	for i := 0; i < n; i++ {
		ans[i] = c1[color1[i]] + best2
	}
	return ans
}

func buildTree3373(n int, edges [][]int) [][]int {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	return g
}

func bipartiteCount(g [][]int, color []int) [2]int {
	n := len(g)
	for i := range color {
		color[i] = -1
	}
	q := []int{0}
	color[0] = 0
	var cnt [2]int
	cnt[0] = 1
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range g[u] {
			if color[v] == -1 {
				color[v] = color[u] ^ 1
				cnt[color[v]]++
				q = append(q, v)
			}
		}
	}
	_ = n
	return cnt
}
