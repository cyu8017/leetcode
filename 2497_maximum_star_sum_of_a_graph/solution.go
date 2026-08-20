// LeetCode 2497 - Maximum Star Sum of a Graph
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

import "sort"

func maxStarSum(vals []int, edges [][]int, k int) int {
	n := len(vals)
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	ans := vals[0]
	for i := 0; i < n; i++ {
		neigh := []int{}
		for _, v := range g[i] {
			if vals[v] > 0 {
				neigh = append(neigh, vals[v])
			}
		}
		sort.Slice(neigh, func(a, b int) bool { return neigh[a] > neigh[b] })
		sum := vals[i]
		for j := 0; j < len(neigh) && j < k; j++ {
			sum += neigh[j]
		}
		if sum > ans {
			ans = sum
		}
	}
	return ans
}
