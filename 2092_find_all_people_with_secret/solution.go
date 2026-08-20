// LeetCode 2092 - Find All People With Secret
// https://leetcode.com/problems/find-all-people-with-secret/

import "sort"

func findAllPeople(n int, meetings [][]int, firstPerson int) []int {
	sort.Slice(meetings, func(i, j int) bool { return meetings[i][2] < meetings[j][2] })
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
	know := make([]bool, n)
	know[0], know[firstPerson] = true, true
	union(0, firstPerson)
	for i := 0; i < len(meetings); {
		j := i
		for j < len(meetings) && meetings[j][2] == meetings[i][2] {
			j++
		}
		for k := i; k < j; k++ {
			union(meetings[k][0], meetings[k][1])
		}
		root0 := find(0)
		reset := []int{}
		for k := i; k < j; k++ {
			a, b := meetings[k][0], meetings[k][1]
			if find(a) != root0 {
				reset = append(reset, a, b)
			} else {
				know[a], know[b] = true, true
			}
		}
		for _, x := range reset {
			parent[x] = x
		}
		i = j
	}
	ans := []int{}
	for i := 0; i < n; i++ {
		if find(i) == find(0) || know[i] {
			ans = append(ans, i)
		}
	}
	return ans
}
