// LeetCode 2403 - Minimum Time to Kill All Monsters
// https://leetcode.com/problems/minimum-time-to-kill-all-monsters/

func minimumTime(power []int) int64 {
	n := len(power)
	N := 1 << n
	dp := make([]int64, N)
	for i := range dp {
		dp[i] = 1 << 60
	}
	dp[0] = 0
	for mask := 0; mask < N; mask++ {
		killed := bits(mask)
		gain := int64(killed + 1)
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			need := (int64(power[i]) + gain - 1) / gain
			nm := mask | (1 << i)
			if dp[mask]+need < dp[nm] {
				dp[nm] = dp[mask] + need
			}
		}
	}
	return dp[N-1]
}

func bits(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
