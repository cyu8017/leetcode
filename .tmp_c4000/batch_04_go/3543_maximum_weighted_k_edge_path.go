// LeetCode 3543 - Maximum Weighted K-Edge Path
// https://leetcode.com/problems/maximum-weighted-k-edge-path/

func maxWeight(n int, edges [][]int, k int, t int) int {
	graph := make([][][2]int, n)
	for _, e := range edges {
		graph[e[0]] = append(graph[e[0]], [2]int{e[1], e[2]})
	}
	dp := make([][]map[int]struct{}, n)
	for u := 0; u < n; u++ {
		dp[u] = make([]map[int]struct{}, k+1)
		for i := 0; i <= k; i++ {
			dp[u][i] = map[int]struct{}{}
		}
		dp[u][0][0] = struct{}{}
	}
	for i := 0; i < k; i++ {
		for u := 0; u < n; u++ {
			for sum := range dp[u][i] {
				for _, e := range graph[u] {
					ns := sum + e[1]
					if ns < t {
						dp[e[0]][i+1][ns] = struct{}{}
					}
				}
			}
		}
	}
	ans := -1
	for u := 0; u < n; u++ {
		for sum := range dp[u][k] {
			if sum > ans {
				ans = sum
			}
		}
	}
	return ans
}
