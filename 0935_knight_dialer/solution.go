// LeetCode 0935 - Knight Dialer
// https://leetcode.com/problems/knight-dialer/

func knightDialer(n int) int {
	const MOD = 1000000007
	moves := [][]int{
		{4, 6},
		{6, 8},
		{7, 9},
		{4, 8},
		{0, 3, 9},
		{},
		{0, 1, 7},
		{2, 6},
		{1, 3},
		{2, 4},
	}
	dp := make([]int, 10)
	for i := range dp {
		dp[i] = 1
	}
	for step := 0; step < n-1; step++ {
		ndp := make([]int, 10)
		for i := 0; i < 10; i++ {
			for _, j := range moves[i] {
				ndp[j] = (ndp[j] + dp[i]) % MOD
			}
		}
		dp = ndp
	}
	ans := 0
	for _, v := range dp {
		ans = (ans + v) % MOD
	}
	return ans
}
