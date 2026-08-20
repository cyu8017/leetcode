// LeetCode 2742 - Painting the Walls
// https://leetcode.com/problems/painting-the-walls/


func paintWalls(cost []int, time []int) int {
	n := len(cost)
	const INF = int(1e18)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	for i := 0; i < n; i++ {
		for j := n; j >= 0; j-- {
			nj := j + time[i] + 1
			if nj > n {
				nj = n
			}
			if dp[j]+cost[i] < dp[nj] {
				dp[nj] = dp[j] + cost[i]
			}
		}
	}
	return dp[n]
}
