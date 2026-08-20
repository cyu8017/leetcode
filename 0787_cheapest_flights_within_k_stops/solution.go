// LeetCode 0787 - Cheapest Flights Within K Stops
// https://leetcode.com/problems/cheapest-flights-within-k-stops/

func findCheapestPrice(n int, flights [][]int, src int, dst int, k int) int {
	const inf = int(^uint(0) >> 1)
	dist := make([]int, n)
	for i := range dist {
		dist[i] = inf
	}
	dist[src] = 0
	for t := 0; t <= k; t++ {
		nxt := append([]int{}, dist...)
		for _, f := range flights {
			u, v, price := f[0], f[1], f[2]
			if dist[u] != inf && dist[u]+price < nxt[v] {
				nxt[v] = dist[u] + price
			}
		}
		dist = nxt
	}
	if dist[dst] == inf {
		return -1
	}
	return dist[dst]
}
