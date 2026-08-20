// LeetCode 0990 - Satisfiability of Equality Equations
// https://leetcode.com/problems/satisfiability-of-equality-equations/

func equationsPossible(equations []string) bool {
	parent := make([]int, 26)
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
	for _, eq := range equations {
		if eq[1] == '=' {
			parent[find(int(eq[0]-'a'))] = find(int(eq[3] - 'a'))
		}
	}
	for _, eq := range equations {
		if eq[1] == '!' && find(int(eq[0]-'a')) == find(int(eq[3]-'a')) {
			return false
		}
	}
	return true
}
