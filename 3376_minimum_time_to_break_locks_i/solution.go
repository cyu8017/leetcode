// LeetCode 3376 - Minimum Time to Break Locks I
// https://leetcode.com/problems/minimum-time-to-break-locks-i/

func findMinimumTime(strength []int, k int) int {
	n := len(strength)
	const inf = int(1e9)
	N := 1 << n
	dp := make([]int, N)
	for i := range dp {
		dp[i] = inf
	}
	dp[0] = 0
	for mask := 0; mask < N; mask++ {
		if dp[mask] == inf {
			continue
		}
		opened := bitsOnes(mask)
		x := 1 + opened*k
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				continue
			}
			t := (strength[i] + x - 1) / x
			nmask := mask | (1 << i)
			if dp[mask]+t < dp[nmask] {
				dp[nmask] = dp[mask] + t
			}
		}
	}
	return dp[N-1]
}

func bitsOnes(x int) int {
	c := 0
	for x > 0 {
		c += x & 1
		x >>= 1
	}
	return c
}
