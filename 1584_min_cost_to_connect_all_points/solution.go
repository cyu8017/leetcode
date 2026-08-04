// LeetCode 1584 - Min Cost to Connect All Points
// https://leetcode.com/problems/min-cost-to-connect-all-points/

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func minCostConnectPoints(points [][]int) int {
	n := len(points)
	used := make([]bool, n)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = 1_000_000_000
	}
	dist[0] = 0
	answer := 0
	for t := 0; t < n; t++ {
		u := -1
		for i := 0; i < n; i++ {
			if !used[i] && (u == -1 || dist[i] < dist[u]) {
				u = i
			}
		}
		used[u] = true
		answer += dist[u]
		for v := 0; v < n; v++ {
			if !used[v] {
				d := abs(points[u][0]-points[v][0]) + abs(points[u][1]-points[v][1])
				if d < dist[v] {
					dist[v] = d
				}
			}
		}
	}
	return answer
}
