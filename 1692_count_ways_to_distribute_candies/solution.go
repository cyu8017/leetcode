// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

func waysToDistribute(n, k int) int {
	const mod = 1000000007
	dp := make([]int, k+1)
	dp[0] = 1
	for i := 1; i <= n; i++ {
		limit := i
		if k < limit {
			limit = k
		}
		for j := limit; j >= 1; j-- {
			dp[j] = (dp[j-1] + j*dp[j]) % mod
		}
		dp[0] = 0
	}
	return dp[k]
}
