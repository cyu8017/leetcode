// LeetCode 1489 - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
// https://leetcode.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/

import "sort"

func findCriticalAndPseudoCriticalEdges(n int, edges [][]int) [][]int {
	type edge struct{ w, a, b, i int }
	es := make([]edge, len(edges))
	for i, e := range edges {
		es[i] = edge{e[2], e[0], e[1], i}
	}
	sort.Slice(es, func(i, j int) bool { return es[i].w < es[j].w })
	const inf = int(1e18)
	mst := func(skip, force int) int {
		parent := make([]int, n)
		for i := range parent {
			parent[i] = i
		}
		var find func(int) int
		find = func(x int) int {
			for x != parent[x] {
				parent[x] = parent[parent[x]]
				x = parent[x]
			}
			return x
		}
		total, used := 0, 0
		if force >= 0 {
			e := es[force]
			parent[find(e.a)] = find(e.b)
			total += e.w
			used++
		}
		for j, e := range es {
			if j == skip || j == force {
				continue
			}
			x, y := find(e.a), find(e.b)
			if x != y {
				parent[x] = y
				total += e.w
				used++
			}
		}
		if used == n-1 {
			return total
		}
		return inf
	}
	base := mst(-1, -1)
	critical, pseudo := []int{}, []int{}
	for j, e := range es {
		if mst(j, -1) > base {
			critical = append(critical, e.i)
		} else if mst(-1, j) == base {
			pseudo = append(pseudo, e.i)
		}
	}
	sort.Ints(critical)
	sort.Ints(pseudo)
	return [][]int{critical, pseudo}
}
