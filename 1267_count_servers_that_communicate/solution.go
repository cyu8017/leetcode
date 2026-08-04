// LeetCode 1267 - Count Servers that Communicate
// https://leetcode.com/problems/count-servers-that-communicate/

func countServers(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	rows := make([]int, m)
	cols := make([]int, n)
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			rows[r] += grid[r][c]
			cols[c] += grid[r][c]
		}
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 && (rows[r] > 1 || cols[c] > 1) {
				ans++
			}
		}
	}
	return ans
}
