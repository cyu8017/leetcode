// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/

func frogPosition(n int, edges [][]int, t int, target int) float64 {
	g := make([][]int, n+1)
	for _, e := range edges {
		a, b := e[0], e[1]
		g[a] = append(g[a], b)
		g[b] = append(g[b], a)
	}
	var dfs func(u, p, time int, prob float64) float64
	dfs = func(u, p, time int, prob float64) float64 {
		kids := []int{}
		for _, v := range g[u] {
			if v != p {
				kids = append(kids, v)
			}
		}
		if time == t || len(kids) == 0 {
			if u == target {
				return prob
			}
			return 0
		}
		sum := 0.0
		for _, v := range kids {
			sum += dfs(v, u, time+1, prob/float64(len(kids)))
		}
		return sum
	}
	return dfs(1, 0, 0, 1.0)
}
