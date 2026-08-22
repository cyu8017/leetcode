// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

func numberOfComponents(properties [][]int, k int) int {
	n := len(properties)
	sets := make([]map[int]bool, n)
	for i, row := range properties {
		sets[i] = map[int]bool{}
		for _, v := range row {
			sets[i][v] = true
		}
	}
	parent := make([]int, n)
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
			parent[ra] = rb
		}
	}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			cnt := 0
			for v := range sets[i] {
				if sets[j][v] {
					cnt++
				}
			}
			if cnt >= k {
				union(i, j)
			}
		}
	}
	comp := map[int]bool{}
	for i := 0; i < n; i++ {
		comp[find(i)] = true
	}
	return len(comp)
}
