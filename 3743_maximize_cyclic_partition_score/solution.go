// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

func maximumScore(nums []int, k int) int64 {
	n := len(nums)
	a := append(append([]int{}, nums...), nums...)
	if k > n {
		k = n
	}
	var best int64
	for start := 0; start < n; start++ {
		seg := a[start : start+n]
		dp := make([][]int64, n+1)
		for i := range dp {
			dp[i] = make([]int64, k+1)
			for j := range dp[i] {
				dp[i][j] = -1 << 60
			}
		}
		dp[0][0] = 0
		for i := 1; i <= n; i++ {
			for j := 1; j <= k && j <= i; j++ {
				mx := int64(-1 << 60)
				for t := i; t >= j; t-- {
					if int64(seg[t-1]) > mx {
						mx = int64(seg[t-1])
					}
					if dp[t-1][j-1] > -1<<60 {
						cand := dp[t-1][j-1] + mx
						if cand > dp[i][j] {
							dp[i][j] = cand
						}
					}
				}
			}
		}
		if dp[n][k] > best {
			best = dp[n][k]
		}
	}
	return best
}
