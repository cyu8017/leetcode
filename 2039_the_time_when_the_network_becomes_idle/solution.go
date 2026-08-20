// LeetCode 2039 - The Time When the Network Becomes Idle
// https://leetcode.com/problems/the-time-when-the-network-becomes-idle/

func networkBecomesIdle(edges [][]int, patience []int) int {
	n := len(patience)
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
		g[e[1]] = append(g[e[1]], e[0])
	}
	dist := make([]int, n)
	for i := range dist {
		dist[i] = -1
	}
	q := []int{0}
	dist[0] = 0
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range g[u] {
			if dist[v] == -1 {
				dist[v] = dist[u] + 1
				q = append(q, v)
			}
		}
	}
	ans := 0
	for i := 1; i < n; i++ {
		round := dist[i] * 2
		lastSend := (round - 1) / patience[i] * patience[i]
		finish := lastSend + round
		if finish > ans {
			ans = finish
		}
	}
	return ans + 1
}
