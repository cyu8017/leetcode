// LeetCode 0827 - Making A Large Island
// https://leetcode.com/problems/making-a-large-island/

func largestIsland(grid [][]int) int {
	n := len(grid)
	sizes := map[int]int{0: 0}
	islandID := 2
	var dfs func(int, int, int) int
	dfs = func(r, c, iid int) int {
		if r < 0 || r >= n || c < 0 || c >= n || grid[r][c] != 1 {
			return 0
		}
		grid[r][c] = iid
		return 1 + dfs(r+1, c, iid) + dfs(r-1, c, iid) + dfs(r, c+1, iid) + dfs(r, c-1, iid)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				sizes[islandID] = dfs(i, j, islandID)
				islandID++
			}
		}
	}
	ans := 0
	for _, v := range sizes {
		if v > ans {
			ans = v
		}
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] != 0 {
				continue
			}
			seen := map[int]bool{}
			total := 1
			for _, d := range dirs {
				ni, nj := i+d[0], j+d[1]
				if ni >= 0 && ni < n && nj >= 0 && nj < n {
					iid := grid[ni][nj]
					if iid > 1 && !seen[iid] {
						seen[iid] = true
						total += sizes[iid]
					}
				}
			}
			if total > ans {
				ans = total
			}
		}
	}
	return ans
}
