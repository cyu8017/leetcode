// LeetCode 2077 - Paths in Maze That Lead to Same Room
// https://leetcode.com/problems/paths-in-maze-that-lead-to-same-room/

func numberOfPaths(n int, corridors [][]int) int {
	g := make([]map[int]bool, n+1)
	for i := range g {
		g[i] = map[int]bool{}
	}
	for _, e := range corridors {
		a, b := e[0], e[1]
		if a > b {
			a, b = b, a
		}
		g[a][b] = true
		g[b][a] = true
	}
	ans := 0
	for _, e := range corridors {
		a, b := e[0], e[1]
		for c := range g[a] {
			if g[b][c] {
				ans++
			}
		}
	}
	return ans / 3
}
