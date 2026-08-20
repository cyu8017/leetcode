// LeetCode 2812 - Find the Safest Path in a Grid
// https://leetcode.com/problems/find-the-safest-path-in-a-grid/

func maximumSafenessFactor(grid [][]int) int {
	n := len(grid)
	dist := make([][]int, n)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	q := [][2]int{}
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 1 {
				dist[i][j] = 0
				q = append(q, [2]int{i, j})
			}
		}
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		for _, d := range dirs {
			ni, nj := cur[0]+d[0], cur[1]+d[1]
			if ni >= 0 && nj >= 0 && ni < n && nj < n && dist[ni][nj] == -1 {
				dist[ni][nj] = dist[cur[0]][cur[1]] + 1
				q = append(q, [2]int{ni, nj})
			}
		}
	}
	ok := func(sf int) bool {
		if dist[0][0] < sf {
			return false
		}
		seen := make([][]bool, n)
		for i := range seen {
			seen[i] = make([]bool, n)
		}
		st := [][2]int{{0, 0}}
		seen[0][0] = true
		for len(st) > 0 {
			cur := st[len(st)-1]
			st = st[:len(st)-1]
			if cur[0] == n-1 && cur[1] == n-1 {
				return true
			}
			for _, d := range dirs {
				ni, nj := cur[0]+d[0], cur[1]+d[1]
				if ni >= 0 && nj >= 0 && ni < n && nj < n && !seen[ni][nj] && dist[ni][nj] >= sf {
					seen[ni][nj] = true
					st = append(st, [2]int{ni, nj})
				}
			}
		}
		return false
	}
	lo, hi, ans := 0, n*n, 0
	for lo <= hi {
		mid := (lo + hi) / 2
		if ok(mid) {
			ans = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}
