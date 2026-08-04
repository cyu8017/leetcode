// LeetCode 1101 - The Earliest Moment When Everyone Become Friends
// https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/

import "sort"

func earliestAcq(logs [][]int, n int) int {
	parent := make([]int, n)
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
	union := func(a, b int) bool {
		ra, rb := find(a), find(b)
		if ra == rb {
			return false
		}
		parent[rb] = ra
		return true
	}
	sort.Slice(logs, func(i, j int) bool { return logs[i][0] < logs[j][0] })
	components := n
	for _, log := range logs {
		if union(log[1], log[2]) {
			components--
			if components == 1 {
				return log[0]
			}
		}
	}
	return -1
}
