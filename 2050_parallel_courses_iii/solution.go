// LeetCode 2050 - Parallel Courses III
// https://leetcode.com/problems/parallel-courses-iii/

func minimumTime(n int, relations [][]int, time []int) int {
	g := make([][]int, n+1)
	indeg := make([]int, n+1)
	for _, e := range relations {
		g[e[0]] = append(g[e[0]], e[1])
		indeg[e[1]]++
	}
	dist := make([]int, n+1)
	q := []int{}
	for i := 1; i <= n; i++ {
		dist[i] = time[i-1]
		if indeg[i] == 0 {
			q = append(q, i)
		}
	}
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, v := range g[u] {
			if dist[u]+time[v-1] > dist[v] {
				dist[v] = dist[u] + time[v-1]
			}
			indeg[v]--
			if indeg[v] == 0 {
				q = append(q, v)
			}
		}
	}
	ans := 0
	for i := 1; i <= n; i++ {
		if dist[i] > ans {
			ans = dist[i]
		}
	}
	return ans
}
