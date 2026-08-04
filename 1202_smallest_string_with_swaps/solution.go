// LeetCode 1202 - Smallest String With Swaps
// https://leetcode.com/problems/smallest-string-with-swaps/

import "sort"

func smallestStringWithSwaps(s string, pairs [][]int) string {
	parent := make([]int, len(s))
	for i := range parent {
		parent[i] = i
	}
	var find func(int) int
	find = func(x int) int {
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	for _, p := range pairs {
		ra, rb := find(p[0]), find(p[1])
		parent[ra] = rb
	}
	groups := map[int][]byte{}
	for i := 0; i < len(s); i++ {
		r := find(i)
		groups[r] = append(groups[r], s[i])
	}
	for r := range groups {
		sort.Slice(groups[r], func(i, j int) bool { return groups[r][i] > groups[r][j] })
	}
	out := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		r := find(i)
		g := groups[r]
		out[i] = g[len(g)-1]
		groups[r] = g[:len(g)-1]
	}
	return string(out)
}
