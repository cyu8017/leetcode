// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

func maxKDivisibleComponents(n int, edges [][]int, values []int, k int) int {
	g := make([][]int, n)
	for _, e := range edges {
		u, v := e[0], e[1]
		g[u] = append(g[u], v)
		g[v] = append(g[v], u)
	}
	ans := 0
	var dfs func(int, int) int
	dfs = func(u, p int) int {
		sum := values[u] % k
		for _, v := range g[u] {
			if v == p {
				continue
			}
			sum = (sum + dfs(v, u)) % k
		}
		if sum == 0 {
			ans++
		}
		return sum
	}
	dfs(0, -1)
	return ans
}
