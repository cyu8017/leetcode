// LeetCode 3459 - Length of Longest V-Shaped Diagonal Segment
// https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/

func lenOfVDiagonal(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	dirs := [][2]int{{1, 1}, {1, -1}, {-1, -1}, {-1, 1}}
	// turn clockwise
	nextDir := []int{1, 2, 3, 0}
	ans := 0
	var dfs func(i, j, d, turned, expect int) int
	memo := map[[5]int]int{}
	dfs = func(i, j, d, turned, expect int) int {
		if i < 0 || j < 0 || i >= m || j >= n || grid[i][j] != expect {
			return 0
		}
		key := [5]int{i, j, d, turned, expect}
		if v, ok := memo[key]; ok {
			return v
		}
		ni, nj := i+dirs[d][0], j+dirs[d][1]
		nx := 0
		if expect == 2 {
			nx = 0
		} else {
			nx = 2
		}
		best := 1 + dfs(ni, nj, d, turned, nx)
		if turned == 0 {
			nd := nextDir[d]
			ti, tj := i+dirs[nd][0], j+dirs[nd][1]
			cand := 1 + dfs(ti, tj, nd, 1, nx)
			if cand > best {
				best = cand
			}
		}
		memo[key] = best
		return best
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != 1 {
				continue
			}
			for d := 0; d < 4; d++ {
				ni, nj := i+dirs[d][0], j+dirs[d][1]
				best := 1 + dfs(ni, nj, d, 0, 2)
				if best > ans {
					ans = best
				}
			}
			if ans < 1 {
				ans = 1
			}
		}
	}
	return ans
}
