// LeetCode 1254 - Number of Closed Islands
// https://leetcode.com/problems/number-of-closed-islands/

func closedIsland(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	flood := func(sr, sc int) bool {
		stack := [][2]int{{sr, sc}}
		grid[sr][sc] = 1
		closed := true
		for len(stack) > 0 {
			cur := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			r, c := cur[0], cur[1]
			if r == 0 || r == m-1 || c == 0 || c == n-1 {
				closed = false
			}
			for _, d := range [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}} {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 0 {
					grid[nr][nc] = 1
					stack = append(stack, [2]int{nr, nc})
				}
			}
		}
		return closed
	}
	ans := 0
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 0 && flood(r, c) {
				ans++
			}
		}
	}
	return ans
}
