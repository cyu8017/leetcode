// LeetCode 2787 - Ways to Express an Integer as Sum of Powers
// https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/

func numberOfWays(n int, x int) int {
	const mod = 1_000_000_007
	powers := []int{}
	for i := 1; ; i++ {
		p := 1
		for j := 0; j < x; j++ {
			p *= i
			if p > n {
				break
			}
		}
		if p > n {
			break
		}
		powers = append(powers, p)
	}
	dp := make([]int, n+1)
	dp[0] = 1
	for _, p := range powers {
		for s := n; s >= p; s-- {
			dp[s] = (dp[s] + dp[s-p]) % mod
		}
	}
	return dp[n]
}
