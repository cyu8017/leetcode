// LeetCode 1926 - Nearest Exit from Entrance in Maze
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

func nearestExit(maze [][]byte, entrance []int) int {
	m, n := len(maze), len(maze[0])
	er, ec := entrance[0], entrance[1]
	type cell struct{ r, c, d int }
	q := []cell{{er, ec, 0}}
	maze[er][ec] = '+'
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, d := range dirs {
			nr, nc := cur.r+d[0], cur.c+d[1]
			if nr >= 0 && nr < m && nc >= 0 && nc < n && maze[nr][nc] == '.' {
				if nr == 0 || nr == m-1 || nc == 0 || nc == n-1 {
					return cur.d + 1
				}
				maze[nr][nc] = '+'
				q = append(q, cell{nr, nc, cur.d + 1})
			}
		}
	}
	return -1
}
