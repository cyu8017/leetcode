// LeetCode 1203 - Sort Items by Groups Respecting Dependencies
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/

func sortItems(n int, m int, group []int, beforeItems [][]int) []int {
	group = append([]int{}, group...)
	for i := 0; i < n; i++ {
		if group[i] == -1 {
			group[i] = m
			m++
		}
	}
	itemGraph := make([][]int, n)
	itemIndeg := make([]int, n)
	groupGraph := make([]map[int]bool, m)
	for i := range groupGraph {
		groupGraph[i] = map[int]bool{}
	}
	groupIndeg := make([]int, m)
	for v := 0; v < n; v++ {
		for _, u := range beforeItems[v] {
			itemGraph[u] = append(itemGraph[u], v)
			itemIndeg[v]++
			if group[u] != group[v] && !groupGraph[group[u]][group[v]] {
				groupGraph[group[u]][group[v]] = true
				groupIndeg[group[v]]++
			}
		}
	}
	topo := func(graph [][]int, indeg []int) []int {
		q := []int{}
		for i, d := range indeg {
			if d == 0 {
				q = append(q, i)
			}
		}
		order := []int{}
		for len(q) > 0 {
			u := q[0]
			q = q[1:]
			order = append(order, u)
			for _, v := range graph[u] {
				indeg[v]--
				if indeg[v] == 0 {
					q = append(q, v)
				}
			}
		}
		if len(order) != len(graph) {
			return nil
		}
		return order
	}
	gAdj := make([][]int, m)
	for u := 0; u < m; u++ {
		for v := range groupGraph[u] {
			gAdj[u] = append(gAdj[u], v)
		}
	}
	items := topo(itemGraph, itemIndeg)
	groups := topo(gAdj, groupIndeg)
	if items == nil || groups == nil {
		return []int{}
	}
	buckets := make([][]int, m)
	for _, item := range items {
		buckets[group[item]] = append(buckets[group[item]], item)
	}
	ans := []int{}
	for _, g := range groups {
		ans = append(ans, buckets[g]...)
	}
	return ans
}
