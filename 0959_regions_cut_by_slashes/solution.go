// LeetCode 0959 - Regions Cut By Slashes
// https://leetcode.com/problems/regions-cut-by-slashes/

func regionsBySlashes(grid []string) int {
	n := len(grid)
	parent := make([]int, n*n*4)
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
	union := func(a, b int) {
		parent[find(a)] = find(b)
	}
	for r := 0; r < n; r++ {
		for c := 0; c < n; c++ {
			root := 4 * (r*n + c)
			ch := grid[r][c]
			if ch == '/' {
				union(root+0, root+3)
				union(root+1, root+2)
			} else if ch == '\\' {
				union(root+0, root+1)
				union(root+2, root+3)
			} else {
				union(root+0, root+1)
				union(root+1, root+2)
				union(root+2, root+3)
			}
			if r+1 < n {
				union(root+2, root+4*n+0)
			}
			if c+1 < n {
				union(root+1, root+4+3)
			}
		}
	}
	ans := 0
	for i := 0; i < n*n*4; i++ {
		if find(i) == i {
			ans++
		}
	}
	return ans
}
