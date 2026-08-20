// LeetCode 0629 - K Inverse Pairs Array
// https://leetcode.com/problems/k-inverse-pairs-array/

func kInversePairs(n int, k int) int {
	const mod = 1000000007
	dp := make([]int, k+1)
	dp[0] = 1
	for size := 1; size <= n; size++ {
		nxt := make([]int, k+1)
		prefix := 0
		for pairs := 0; pairs <= k; pairs++ {
			prefix = (prefix + dp[pairs]) % mod
			if pairs >= size {
				prefix = (prefix - dp[pairs-size]) % mod
				if prefix < 0 {
					prefix += mod
				}
			}
			nxt[pairs] = prefix
		}
		dp = nxt
	}
	return dp[k]
}
