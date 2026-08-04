// LeetCode 1319 - Number of Operations to Make Network Connected
// https://leetcode.com/problems/number-of-operations-to-make-network-connected/

func makeConnected(n int, connections [][]int) int {
	if len(connections) < n-1 {
		return -1
	}
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
	for _, e := range connections {
		ra, rb := find(e[0]), find(e[1])
		if ra != rb {
			parent[ra] = rb
		}
	}
	comps := map[int]bool{}
	for i := 0; i < n; i++ {
		comps[find(i)] = true
	}
	return len(comps) - 1
}
