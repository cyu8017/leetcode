// LeetCode 1765 - Map of Highest Peak
// https://leetcode.com/problems/map-of-highest-peak/

func highestPeak(isWater [][]int) [][]int {
	m, n := len(isWater), len(isWater[0])
	dist := make([][]int, m)
	for i := range dist {
		dist[i] = make([]int, n)
		for j := range dist[i] {
			dist[i][j] = -1
		}
	}
	queue := make([][2]int, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if isWater[i][j] == 1 {
				dist[i][j] = 0
				queue = append(queue, [2]int{i, j})
			}
		}
	}
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for head := 0; head < len(queue); head++ {
		i, j := queue[head][0], queue[head][1]
		for _, d := range dirs {
			x, y := i+d[0], j+d[1]
			if x >= 0 && x < m && y >= 0 && y < n && dist[x][y] == -1 {
				dist[x][y] = dist[i][j] + 1
				queue = append(queue, [2]int{x, y})
			}
		}
	}
	return dist
}
