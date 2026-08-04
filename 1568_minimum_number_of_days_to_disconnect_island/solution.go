// LeetCode 1568 - Minimum Number of Days to Disconnect Island
// https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/

func minDays(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	islands := func() int {
		seen := make([][]bool, m)
		for i := range seen {
			seen[i] = make([]bool, n)
		}
		count := 0
		dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		for r := 0; r < m; r++ {
			for c := 0; c < n; c++ {
				if grid[r][c] == 1 && !seen[r][c] {
					count++
					stack := [][2]int{{r, c}}
					seen[r][c] = true
					for len(stack) > 0 {
						x, y := stack[len(stack)-1][0], stack[len(stack)-1][1]
						stack = stack[:len(stack)-1]
						for _, d := range dirs {
							nx, ny := x+d[0], y+d[1]
							if nx >= 0 && nx < m && ny >= 0 && ny < n && grid[nx][ny] == 1 && !seen[nx][ny] {
								seen[nx][ny] = true
								stack = append(stack, [2]int{nx, ny})
							}
						}
					}
				}
			}
		}
		return count
	}
	if islands() != 1 {
		return 0
	}
	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if grid[r][c] == 1 {
				grid[r][c] = 0
				if islands() != 1 {
					grid[r][c] = 1
					return 1
				}
				grid[r][c] = 1
			}
		}
	}
	return 2
}
