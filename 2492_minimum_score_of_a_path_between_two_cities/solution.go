// LeetCode 2492 - Minimum Score of a Path Between Two Cities
// https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

func minScore(n int, roads [][]int) int {
	g := make([][][2]int, n+1)
	for _, r := range roads {
		g[r[0]] = append(g[r[0]], [2]int{r[1], r[2]})
		g[r[1]] = append(g[r[1]], [2]int{r[0], r[2]})
	}
	vis := make([]bool, n+1)
	ans := 1 << 30
	q := []int{1}
	vis[1] = true
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		for _, e := range g[u] {
			if e[1] < ans {
				ans = e[1]
			}
			if !vis[e[0]] {
				vis[e[0]] = true
				q = append(q, e[0])
			}
		}
	}
	return ans
}
