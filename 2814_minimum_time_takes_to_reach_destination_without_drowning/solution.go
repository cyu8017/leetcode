// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

func minimumSeconds(land [][]string) int {
	m, n := len(land), len(land[0])
	const inf = 1 << 30
	water := make([][]int, m)
	for i := range water {
		water[i] = make([]int, n)
		for j := range water[i] {
			water[i][j] = inf
		}
	}
	wq := [][2]int{}
	var start, dest [2]int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			switch land[i][j] {
			case "*":
				water[i][j] = 0
				wq = append(wq, [2]int{i, j})
			case "S":
				start = [2]int{i, j}
			case "D":
				dest = [2]int{i, j}
			}
		}
	}
	dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(wq) > 0 {
		cur := wq[0]
		wq = wq[1:]
		for _, d := range dirs {
			ni, nj := cur[0]+d[0], cur[1]+d[1]
			if ni < 0 || nj < 0 || ni >= m || nj >= n {
				continue
			}
			if land[ni][nj] == "X" || land[ni][nj] == "D" {
				continue
			}
			if water[ni][nj] > water[cur[0]][cur[1]]+1 {
				water[ni][nj] = water[cur[0]][cur[1]] + 1
				wq = append(wq, [2]int{ni, nj})
			}
		}
	}
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	q := [][2]int{start}
	dist[start[0]][start[1]] = 0
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur == dest {
			return dist[cur[0]][cur[1]]
		}
		for _, d := range dirs {
			ni, nj := cur[0]+d[0], cur[1]+d[1]
			if ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] != -1 {
				continue
			}
			if land[ni][nj] == "X" {
				continue
			}
			nd := dist[cur[0]][cur[1]] + 1
			if land[ni][nj] != "D" && nd >= water[ni][nj] {
				continue
			}
			dist[ni][nj] = nd
			q = append(q, [2]int{ni, nj})
		}
	}
	return -1
}
