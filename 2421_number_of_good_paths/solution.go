// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

import "sort"

func numberOfGoodPaths(vals []int, edges [][]int) int {
	n := len(vals)
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	parent := make([]int, n)
	size := make([]int, n)
	for i := range parent {
		parent[i] = i
		size[i] = 1
	}
	var find func(int) int
	find = func(x int) int {
		if parent[x] != x {
			parent[x] = find(parent[x])
		}
		return parent[x]
	}
	nodes := make([]int, n)
	for i := range nodes {
		nodes[i] = i
	}
	sort.Slice(nodes, func(i, j int) bool { return vals[nodes[i]] < vals[nodes[j]] })
	ans := n
	i := 0
	for i < n {
		j := i
		for j < n && vals[nodes[j]] == vals[nodes[i]] {
			j++
		}
		for k := i; k < j; k++ {
			u := nodes[k]
			for _, v := range g[u] {
				if vals[v] <= vals[u] {
					ru, rv := find(u), find(v)
					if ru != rv {
						parent[ru] = rv
						size[rv] += size[ru]
					}
				}
			}
		}
		freq := map[int]int{}
		for k := i; k < j; k++ {
			freq[find(nodes[k])]++
		}
		for _, c := range freq {
			ans += c * (c - 1) / 2
		}
		i = j
	}
	return ans
}
