// LeetCode 2392 - Build a Matrix With Conditions
// https://leetcode.com/problems/build-a-matrix-with-conditions/

func buildMatrix(k int, rowConditions [][]int, colConditions [][]int) [][]int {
	topo := func(conds [][]int) []int {
		g := make([][]int, k+1)
		indeg := make([]int, k+1)
		for _, c := range conds {
			g[c[0]] = append(g[c[0]], c[1])
			indeg[c[1]]++
		}
		q := []int{}
		for i := 1; i <= k; i++ {
			if indeg[i] == 0 {
				q = append(q, i)
			}
		}
		order := []int{}
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			order = append(order, u)
			for _, v := range g[u] {
				indeg[v]--
				if indeg[v] == 0 {
					q = append(q, v)
				}
			}
		}
		if len(order) != k {
			return nil
		}
		return order
	}
	rowOrder := topo(rowConditions)
	colOrder := topo(colConditions)
	if rowOrder == nil || colOrder == nil {
		return [][]int{}
	}
	rowPos := make([]int, k+1)
	colPos := make([]int, k+1)
	for i, v := range rowOrder {
		rowPos[v] = i
	}
	for i, v := range colOrder {
		colPos[v] = i
	}
	ans := make([][]int, k)
	for i := range ans {
		ans[i] = make([]int, k)
	}
	for v := 1; v <= k; v++ {
		ans[rowPos[v]][colPos[v]] = v
	}
	return ans
}
