// LeetCode 0947 - Most Stones Removed with Same Row or Column
// https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

func removeStones(stones [][]int) int {
	parent := map[int]int{}
	var find func(int) int
	find = func(x int) int {
		if _, ok := parent[x]; !ok {
			parent[x] = x
		}
		for parent[x] != x {
			parent[x] = parent[parent[x]]
			x = parent[x]
		}
		return x
	}
	union := func(a, b int) {
		parent[find(a)] = find(b)
	}
	for _, s := range stones {
		union(s[0], ^s[1])
	}
	roots := map[int]bool{}
	for _, s := range stones {
		roots[find(s[0])] = true
	}
	return len(stones) - len(roots)
}
