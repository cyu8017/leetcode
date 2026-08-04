// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

func numWays(steps int, arrLen int) int {
	const mod = 1000000007
	width := arrLen
	if steps/2+1 < width {
		width = steps/2 + 1
	}
	dp := make([]int, width)
	dp[0] = 1
	for step := 0; step < steps; step++ {
		nxt := make([]int, width)
		for i := 0; i < width; i++ {
			nxt[i] = dp[i]
			if i > 0 {
				nxt[i] = (nxt[i] + dp[i-1]) % mod
			}
			if i+1 < width {
				nxt[i] = (nxt[i] + dp[i+1]) % mod
			}
		}
		dp = nxt
	}
	return dp[0]
}
