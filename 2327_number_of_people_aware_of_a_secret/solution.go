// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

func peopleAwareOfSecret(n int, delay int, forget int) int {
	const mod = 1000000007
	dp := make([]int, n+1)
	dp[1] = 1
	share := 0
	for day := 2; day <= n; day++ {
		if day-delay >= 1 {
			share = (share + dp[day-delay]) % mod
		}
		if day-forget >= 1 {
			share = (share - dp[day-forget] + mod) % mod
		}
		dp[day] = share
	}
	ans := 0
	for day := n - forget + 1; day <= n; day++ {
		if day >= 1 {
			ans = (ans + dp[day]) % mod
		}
	}
	return ans
}
