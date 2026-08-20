// LeetCode 2061 - Number of Spaces Cleaning Robot Cleaned
// https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/

func numberOfCleanRooms(room [][]int) int {
	m, n := len(room), len(room[0])
	dirs := [][2]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}
	vis := map[[3]int]bool{}
	cleaned := map[[2]int]bool{{0, 0}: true}
	r, c, d := 0, 0, 0
	for !vis[[3]int{r, c, d}] {
		vis[[3]int{r, c, d}] = true
		nr, nc := r+dirs[d][0], c+dirs[d][1]
		if nr >= 0 && nr < m && nc >= 0 && nc < n && room[nr][nc] == 0 {
			r, c = nr, nc
			cleaned[[2]int{r, c}] = true
		} else {
			d = (d + 1) % 4
		}
	}
	return len(cleaned)
}
