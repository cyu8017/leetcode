// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

import "sort"

func matrixRankTransform(matrix [][]int) [][]int {
	m, n := len(matrix), len(matrix[0])
	type pair struct{ i, j int }
	groups := map[int][]pair{}
	vals := []int{}
	seen := map[int]bool{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			v := matrix[i][j]
			groups[v] = append(groups[v], pair{i, j})
			if !seen[v] {
				seen[v] = true
				vals = append(vals, v)
			}
		}
	}
	sort.Ints(vals)
	rank := make([]int, m+n)
	ans := make([][]int, m)
	for i := range ans {
		ans[i] = make([]int, n)
	}
	for _, value := range vals {
		parent := map[int]int{}
		var find func(int) int
		find = func(x int) int {
			if _, ok := parent[x]; !ok {
				parent[x] = x
			}
			if parent[x] != x {
				parent[x] = find(parent[x])
			}
			return parent[x]
		}
		for _, p := range groups[value] {
			a, b := find(p.i), find(m+p.j)
			parent[a] = b
		}
		best := map[int]int{}
		for _, p := range groups[value] {
			r := find(p.i)
			cur := rank[p.i]
			if rank[m+p.j] > cur {
				cur = rank[m+p.j]
			}
			if cur > best[r] {
				best[r] = cur
			}
		}
		for _, p := range groups[value] {
			r := best[find(p.i)] + 1
			ans[p.i][p.j] = r
		}
		for _, p := range groups[value] {
			if ans[p.i][p.j] > rank[p.i] {
				rank[p.i] = ans[p.i][p.j]
			}
			if ans[p.i][p.j] > rank[m+p.j] {
				rank[m+p.j] = ans[p.i][p.j]
			}
		}
	}
	return ans
}
