// LeetCode 3336 - Find the Number of Subsequences With Equal GCD
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/

func subsequencePairCount(nums []int) int {
	const mod = 1000000007
	maxV := 0
	for _, x := range nums {
		if x > maxV {
			maxV = x
		}
	}
	dp := make([][]int, maxV+1)
	for i := range dp {
		dp[i] = make([]int, maxV+1)
	}
	dp[0][0] = 1
	for _, x := range nums {
		ndp := make([][]int, maxV+1)
		for i := range ndp {
			ndp[i] = append([]int(nil), dp[i]...)
		}
		for a := 0; a <= maxV; a++ {
			for b := 0; b <= maxV; b++ {
				if dp[a][b] == 0 {
					continue
				}
				na := gcd3336(a, x)
				if a == 0 {
					na = x
				}
				nb := gcd3336(b, x)
				if b == 0 {
					nb = x
				}
				ndp[na][b] = (ndp[na][b] + dp[a][b]) % mod
				ndp[a][nb] = (ndp[a][nb] + dp[a][b]) % mod
			}
		}
		dp = ndp
	}
	ans := 0
	for g := 1; g <= maxV; g++ {
		ans = (ans + dp[g][g]) % mod
	}
	return ans
}

func gcd3336(a, b int) int {
	if a == 0 {
		return b
	}
	for b != 0 {
		a, b = b, a%b
	}
	return a
}
