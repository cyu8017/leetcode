// LeetCode 3317 - Find the Number of Possible Ways for an Event
// https://leetcode.com/problems/find-the-number-of-possible-ways-for-an-event/

func numberOfWays(n int, x int, y int) int {
	const mod = 1000000007
	// stirling2nd * x!/(x-k)! * y^k for k stages used
	// dp[i][j] = ways to assign i people to j non-empty stages
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, x+1)
	}
	dp[0][0] = 1
	for i := 1; i <= n; i++ {
		for j := 1; j <= x && j <= i; j++ {
			dp[i][j] = (dp[i-1][j-1] + j*dp[i-1][j]%mod) % mod
		}
	}
	fact := make([]int, x+1)
	fact[0] = 1
	for i := 1; i <= x; i++ {
		fact[i] = fact[i-1] * i % mod
	}
	ans := 0
	ypow := 1
	for k := 1; k <= x && k <= n; k++ {
		ypow = ypow * y % mod
		// P(x,k) = x!/(x-k)!
		perm := fact[x] * modInverse(fact[x-k], mod) % mod
		ans = (ans + dp[n][k]*perm%mod*ypow%mod) % mod
	}
	return ans
}

func modInverse(a, mod int) int {
	return modPow(a, mod-2, mod)
}
func modPow(a, e, mod int) int {
	r := 1
	a %= mod
	for e > 0 {
		if e&1 == 1 {
			r = r * a % mod
		}
		a = a * a % mod
		e >>= 1
	}
	return r
}
