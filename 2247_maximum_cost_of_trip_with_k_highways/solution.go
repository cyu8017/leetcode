// LeetCode 2247 - Maximum Cost of Trip With K Highways
// https://leetcode.com/problems/maximum-cost-of-trip-with-k-highways/

func maximumCost(n int, highways [][]int, k int) int {
	if k+1 > n {
		return -1
	}
	g := make([][][2]int, n)
	for _, h := range highways {
		g[h[0]] = append(g[h[0]], [2]int{h[1], h[2]})
		g[h[1]] = append(g[h[1]], [2]int{h[0], h[2]})
	}
	dp := make([][]int, 1<<n)
	for i := range dp {
		dp[i] = make([]int, n)
		for j := range dp[i] {
			dp[i][j] = -1
		}
	}
	for i := 0; i < n; i++ {
		dp[1<<i][i] = 0
	}
	ans := -1
	for mask := 0; mask < 1<<n; mask++ {
		cities := bitsCount2247(mask)
		for u := 0; u < n; u++ {
			if dp[mask][u] < 0 {
				continue
			}
			if cities-1 == k && dp[mask][u] > ans {
				ans = dp[mask][u]
			}
			for _, e := range g[u] {
				v, w := e[0], e[1]
				if mask&(1<<v) != 0 {
					continue
				}
				nm := mask | (1 << v)
				cand := dp[mask][u] + w
				if cand > dp[nm][v] {
					dp[nm][v] = cand
				}
			}
		}
	}
	return ans
}

func bitsCount2247(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
