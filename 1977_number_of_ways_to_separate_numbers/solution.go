// LeetCode 1977 - Number of Ways to Separate Numbers
// https://leetcode.com/problems/number-of-ways-to-separate-numbers/

func numberOfCombinations(num string) int {
	const MOD = 1000000007
	n := len(num)
	if num[0] == '0' {
		return 0
	}
	lcp := make([][]int, n+1)
	for i := range lcp {
		lcp[i] = make([]int, n+1)
	}
	for i := n - 1; i >= 0; i-- {
		for j := n - 1; j >= 0; j-- {
			if num[i] == num[j] {
				lcp[i][j] = lcp[i+1][j+1] + 1
			}
		}
	}
	le := func(a, b, length int) bool {
		common := lcp[a][b]
		if common >= length {
			return true
		}
		return num[a+common] < num[b+common]
	}
	dp := make([][]int, n+1)
	pref := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		pref[i] = make([]int, n+1)
	}
	for i := 1; i <= n; i++ {
		for l := 1; l <= i; l++ {
			start := i - l
			if num[start] == '0' {
				dp[i][l] = 0
			} else if start == 0 {
				dp[i][l] = 1
			} else {
				ways := 0
				if l > 1 {
					lim := l - 1
					if start < lim {
						lim = start
					}
					ways = pref[start][lim]
				}
				if start >= l && le(start-l, start, l) {
					ways = (ways + dp[start][l]) % MOD
				}
				dp[i][l] = ways
			}
		}
		for l := 1; l <= n; l++ {
			add := 0
			if l <= i {
				add = dp[i][l]
			}
			pref[i][l] = (pref[i][l-1] + add) % MOD
		}
	}
	return pref[n][n]
}
