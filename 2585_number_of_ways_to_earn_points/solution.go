// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/


func waysToReachTarget(target int, types [][]int) int {
	const MOD = 1000000007
	dp := make([]int, target+1)
	dp[0] = 1
	for _, t := range types {
		count, marks := t[0], t[1]
		for s := target; s >= 0; s-- {
			for k := 1; k <= count && s-k*marks >= 0; k++ {
				dp[s] = (dp[s] + dp[s-k*marks]) % MOD
			}
		}
	}
	return dp[target]
}
