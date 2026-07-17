// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

func rearrangeSticks(n int, k int) int {
	const mod = 1_000_000_007
	if k == 0 || k > n {
		return 0
	}

	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	dp[1][1] = 1

	for sticks := 2; sticks <= n; sticks++ {
		dp[sticks][1] = (sticks - 1) * dp[sticks-1][1] % mod
		for visible := 2; visible <= sticks; visible++ {
			dp[sticks][visible] = (dp[sticks-1][visible-1] + (sticks-1)*dp[sticks-1][visible]) % mod
		}
	}

	return dp[n][k]
}
