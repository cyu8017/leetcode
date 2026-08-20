// LeetCode 3607 - Power Grid Maintenance
// https://leetcode.com/problems/power-grid-maintenance/

import (
	"sort"
)

func processQueries(c int, connections [][]int, queries [][]int) []int {
	parent := make([]int, c+1)
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	union := func(a, b int) {
		ra, rb := find(a), find(b)
		if ra != rb {
			if ra < rb {
				parent[rb] = ra
			} else {
				parent[ra] = rb
			}
		}
	}
	for _, e := range connections {
		union(e[0], e[1])
	}
	online := make([]bool, c+1)
	for i := 1; i <= c; i++ {
		online[i] = true
	}
	// for each component root, maintain sorted set of online ids — use heap/map
	comp := map[int][]int{}
	for i := 1; i <= c; i++ {
		r := find(i)
		comp[r] = append(comp[r], i)
	}
	for r := range comp {
		sort.Ints(comp[r])
	}
	ptr := map[int]int{}
	ans := []int{}
	for _, q := range queries {
		t, x := q[0], q[1]
		if t == 2 {
			online[x] = false
			continue
		}
		if online[x] {
			ans = append(ans, x)
			continue
		}
		r := find(x)
		ids := comp[r]
		for ptr[r] < len(ids) && !online[ids[ptr[r]]] {
			ptr[r]++
		}
		if ptr[r] < len(ids) {
			ans = append(ans, ids[ptr[r]])
		} else {
			ans = append(ans, -1)
		}
	}
	return ans
}
