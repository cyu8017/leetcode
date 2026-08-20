// LeetCode 2318 - Number of Distinct Roll Sequences
// https://leetcode.com/problems/number-of-distinct-roll-sequences/

func distinctSequences(n int) int {
	const mod = 1000000007
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	dp := make([][][]int, n+1)
	for i := range dp {
		dp[i] = make([][]int, 7)
		for j := range dp[i] {
			dp[i][j] = make([]int, 7)
		}
	}
	for a := 1; a <= 6; a++ {
		dp[1][a][0] = 1
	}
	for i := 2; i <= n; i++ {
		for prev := 1; prev <= 6; prev++ {
			for pprev := 0; pprev <= 6; pprev++ {
				if dp[i-1][prev][pprev] == 0 {
					continue
				}
				for cur := 1; cur <= 6; cur++ {
					if cur == prev || cur == pprev || gcd(cur, prev) != 1 {
						continue
					}
					dp[i][cur][prev] = (dp[i][cur][prev] + dp[i-1][prev][pprev]) % mod
				}
			}
		}
	}
	ans := 0
	for a := 1; a <= 6; a++ {
		for b := 0; b <= 6; b++ {
			ans = (ans + dp[n][a][b]) % mod
		}
	}
	return ans
}
