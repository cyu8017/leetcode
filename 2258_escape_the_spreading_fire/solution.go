// LeetCode 2258 - Escape the Spreading Fire
// https://leetcode.com/problems/escape-the-spreading-fire/

func maximumMinutes(grid [][]int) int {
	m, n := len(grid), len(grid[0])
	const inf = 1000000000
	fire := make([][]int, m)
	for i := range fire {
		fire[i] = make([]int, n)
		for j := range fire[i] {
			fire[i][j] = inf
		}
	}
	q := [][2]int{}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				fire[i][j] = 0
				q = append(q, [2]int{i, j})
			}
		}
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, d := range dirs {
			nr, nc := cur[0]+d[0], cur[1]+d[1]
			if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || fire[nr][nc] != inf {
				continue
			}
			fire[nr][nc] = fire[cur[0]][cur[1]] + 1
			q = append(q, [2]int{nr, nc})
		}
	}
	can := func(wait int) bool {
		if wait >= fire[0][0] {
			return false
		}
		vis := make([][]bool, m)
		for i := range vis {
			vis[i] = make([]bool, n)
		}
		type node struct{ r, c, t int }
		qq := []node{{0, 0, wait}}
		vis[0][0] = true
		for len(qq) > 0 {
			cur := qq[0]
			qq = qq[1:]
			for _, d := range dirs {
				nr, nc := cur.r+d[0], cur.c+d[1]
				nt := cur.t + 1
				if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 2 || vis[nr][nc] {
					continue
				}
				if nr == m-1 && nc == n-1 {
					if nt <= fire[nr][nc] {
						return true
					}
					continue
				}
				if nt >= fire[nr][nc] {
					continue
				}
				vis[nr][nc] = true
				qq = append(qq, node{nr, nc, nt})
			}
		}
		return false
	}
	lo, hi := 0, m*n+10
	ans := -1
	for lo <= hi {
		mid := (lo + hi) / 2
		if can(mid) {
			ans = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	if ans >= m*n {
		return inf
	}
	return ans
}
