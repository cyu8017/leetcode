// LeetCode 2174 - Remove All Ones With Row and Column Flips II
// https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips-ii/

func removeOnes(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	ones := [][2]int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				ones = append(ones, [2]int{i, j})
			}
		}
	}
	if len(ones) == 0 {
		return 0
	}
	ans := m + n
	var dfs func(int, int)
	dfs = func(idx, flips int) {
		if flips >= ans {
			return
		}
		for idx < len(ones) && grid[ones[idx][0]][ones[idx][1]] == 0 {
			idx++
		}
		if idx == len(ones) {
			ans = flips
			return
		}
		r, c := ones[idx][0], ones[idx][1]
		// flip row
		changed := [][2]int{}
		for j := 0; j < n; j++ {
			if grid[r][j] == 1 {
				grid[r][j] = 0
				changed = append(changed, [2]int{r, j})
			}
		}
		dfs(idx+1, flips+1)
		for _, p := range changed {
			grid[p[0]][p[1]] = 1
		}
		// flip col
		changed = changed[:0]
		for i := 0; i < m; i++ {
			if grid[i][c] == 1 {
				grid[i][c] = 0
				changed = append(changed, [2]int{i, c})
			}
		}
		dfs(idx+1, flips+1)
		for _, p := range changed {
			grid[p[0]][p[1]] = 1
		}
	}
	dfs(0, 0)
	return ans
}
