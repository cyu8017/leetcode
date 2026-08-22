// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

import "sort"

func minOperations(nums []int, x int, k int) int64 {
	n := len(nums)
	minOps := make([]int64, n-x+1)
	for i := 0; i+x <= n; i++ {
		w := append([]int(nil), nums[i:i+x]...)
		sort.Ints(w)
		med := w[(x-1)/2]
		var ops int64
		for _, v := range w {
			d := v - med
			if d < 0 {
				d = -d
			}
			ops += int64(d)
		}
		minOps[i] = ops
	}
	const inf int64 = 1 << 62
	dp := make([][]int64, n+1)
	for i := range dp {
		dp[i] = make([]int64, k+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[n][0] = 0
	for i := n - 1; i >= 0; i-- {
		for j := 0; j <= k; j++ {
			dp[i][j] = dp[i+1][j]
			if j > 0 && i+x <= n && minOps[i]+dp[i+x][j-1] < dp[i][j] {
				dp[i][j] = minOps[i] + dp[i+x][j-1]
			}
		}
	}
	return dp[0][k]
}
