// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

func dieSimulator(n int, rollMax []int) int {
	const mod = 1000000007
	dp := make([][]int, 6)
	for j := 0; j < 6; j++ {
		dp[j] = make([]int, rollMax[j]+1)
		dp[j][1] = 1
	}
	for step := 1; step < n; step++ {
		totals := make([]int, 6)
		for j := 0; j < 6; j++ {
			for _, v := range dp[j] {
				totals[j] = (totals[j] + v) % mod
			}
		}
		all := 0
		for _, t := range totals {
			all = (all + t) % mod
		}
		nxt := make([][]int, 6)
		for j := 0; j < 6; j++ {
			nxt[j] = make([]int, len(dp[j]))
			nxt[j][1] = (all - totals[j] + mod) % mod
			for run := 2; run < len(dp[j]); run++ {
				nxt[j][run] = dp[j][run-1]
			}
		}
		dp = nxt
	}
	ans := 0
	for j := 0; j < 6; j++ {
		for _, v := range dp[j] {
			ans = (ans + v) % mod
		}
	}
	return ans
}
