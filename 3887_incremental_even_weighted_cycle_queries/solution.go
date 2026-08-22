// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

func countValidEdges(n int, edges [][]int) int {
	parent, size, parity := make([]int, n), make([]int, n), make([]int, n)
	for i := 0; i < n; i++ {
		parent[i], size[i] = i, 1
	}
	var find func(int) (int, int)
	find = func(x int) (int, int) {
		if parent[x] == x {
			return x, 0
		}
		root, p := find(parent[x])
		parity[x] ^= p
		parent[x] = root
		return root, parity[x]
	}
	ans := 0
	for _, e := range edges {
		ru, pu := find(e[0])
		rv, pv := find(e[1])
		if ru == rv {
			if pu^pv == e[2] {
				ans++
			}
			continue
		}
		if size[ru] < size[rv] {
			ru, rv = rv, ru
			pu, pv = pv, pu
		}
		parent[rv] = ru
		parity[rv] = pu ^ pv ^ e[2]
		size[ru] += size[rv]
		ans++
	}
	return ans
}