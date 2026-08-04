// LeetCode 1334 - Find the City With the Smallest Number of Neighbors at a Threshold Distance
// https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

func findTheCity(n int, edges [][]int, distanceThreshold int) int {
	const inf = int64(1e15)
	dist := make([][]int64, n)
	for i := range dist {
		dist[i] = make([]int64, n)
		for j := range dist[i] {
			dist[i][j] = inf
		}
		dist[i][i] = 0
	}
	for _, e := range edges {
		a, b, w := e[0], e[1], int64(e[2])
		dist[a][b], dist[b][a] = w, w
	}
	for k := 0; k < n; k++ {
		for i := 0; i < n; i++ {
			for j := 0; j < n; j++ {
				if dist[i][k]+dist[k][j] < dist[i][j] {
					dist[i][j] = dist[i][k] + dist[k][j]
				}
			}
		}
	}
	bestCity, bestCount := -1, n+1
	for city := 0; city < n; city++ {
		count := 0
		for _, d := range dist[city] {
			if d <= int64(distanceThreshold) {
				count++
			}
		}
		if count <= bestCount {
			bestCount = count
			bestCity = city
		}
	}
	return bestCity
}
