// LeetCode 2646 - Minimize the Total Price of the Trips
// https://leetcode.com/problems/minimize-the-total-price-of-the-trips/


func minimumTotalPrice(n int, edges [][]int, price []int, trips [][]int) int {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	cnt := make([]int, n)
	var path func(u, p, target int) bool
	path = func(u, p, target int) bool {
		if u == target {
			cnt[u]++
			return true
		}
		for _, v := range g[u] {
			if v == p {
				continue
			}
			if path(v, u, target) {
				cnt[u]++
				return true
			}
		}
		return false
	}
	for _, t := range trips {
		path(t[0], -1, t[1])
	}
	var dfs func(u, p int) (int, int) // nothalve, halve
	dfs = func(u, p int) (int, int) {
		full := price[u] * cnt[u]
		half := full / 2
		for _, v := range g[u] {
			if v == p {
				continue
			}
			nf, hf := dfs(v, u)
			full += min2646(nf, hf)
			half += nf
		}
		return full, half
	}
	a, b := dfs(0, -1)
	return min2646(a, b)
}
func min2646(a, b int) int {
	if a < b {
		return a
	}
	return b
}
