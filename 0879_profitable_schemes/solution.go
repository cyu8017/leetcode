// LeetCode 0879 - Profitable Schemes
// https://leetcode.com/problems/profitable-schemes/

func profitableSchemes(n int, minProfit int, group []int, profit []int) int {
	const MOD = 1_000_000_007
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, minProfit+1)
	}
	dp[0][0] = 1
	for idx := range group {
		members, p := group[idx], profit[idx]
		for people := n; people >= members; people-- {
			for prof := minProfit; prof >= 0; prof-- {
				np := prof + p
				if np > minProfit {
					np = minProfit
				}
				dp[people][np] = (dp[people][np] + dp[people-members][prof]) % MOD
			}
		}
	}
	ans := 0
	for people := 0; people <= n; people++ {
		ans = (ans + dp[people][minProfit]) % MOD
	}
	return ans
}
