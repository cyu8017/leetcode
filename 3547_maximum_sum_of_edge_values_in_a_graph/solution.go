// LeetCode 3547 - Maximum Sum of Edge Values in a Graph
// https://leetcode.com/problems/maximum-sum-of-edge-values-in-a-graph/

import (
	"sort"
)

func maxScore(n int, edges [][]int) int64 {
	graph := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		graph[u] = append(graph[u], v)
		graph[v] = append(graph[v], u)
	}
	seen := make([]bool, n)
	var cycleSizes, pathSizes []int
	getComp := func(start int) []int {
		comp := []int{start}
		seen[start] = true
		for i := 0; i < len(comp); i++ {
			for _, v := range graph[comp[i]] {
				if !seen[v] {
					seen[v] = true
					comp = append(comp, v)
				}
			}
		}
		return comp
	}
	for i := 0; i < n; i++ {
		if seen[i] {
			continue
		}
		comp := getComp(i)
		allDeg2 := true
		for _, u := range comp {
			if len(graph[u]) != 2 {
				allDeg2 = false
				break
			}
		}
		if allDeg2 {
			cycleSizes = append(cycleSizes, len(comp))
		} else if len(comp) > 1 {
			pathSizes = append(pathSizes, len(comp))
		}
	}
	calc := func(left, right int, isCycle bool) int64 {
		w0, w1 := right, right
		var score int64
		for value := right - 1; value >= left; value-- {
			score += int64(w0) * int64(value)
			w0, w1 = w1, value
		}
		if isCycle {
			score += int64(w0) * int64(w1)
		}
		return score
	}
	var ans int64
	curN := n
	for _, cs := range cycleSizes {
		ans += calc(curN-cs+1, curN, true)
		curN -= cs
	}
	sort.Sort(sort.Reverse(sort.IntSlice(pathSizes)))
	for _, ps := range pathSizes {
		ans += calc(curN-ps+1, curN, false)
		curN -= ps
	}
	return ans
}
