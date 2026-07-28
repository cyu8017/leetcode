// LeetCode 1000 - Minimum Cost to Merge Stones
// https://leetcode.com/problems/minimum-cost-to-merge-stones/

func mergeStones(stones []int, k int) int {
	n := len(stones)
	if (n-1)%(k-1) != 0 {
		return -1
	}
	prefix := make([]int, n+1)
	for i, x := range stones {
		prefix[i+1] = prefix[i] + x
	}
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	for length := k; length <= n; length++ {
		for i := 0; i+length-1 < n; i++ {
			j := i + length - 1
			best := int(^uint(0) >> 1)
			for m := i; m < j; m += k - 1 {
				if v := dp[i][m] + dp[m+1][j]; v < best {
					best = v
				}
			}
			dp[i][j] = best
			if (length-1)%(k-1) == 0 {
				dp[i][j] += prefix[j+1] - prefix[i]
			}
		}
	}
	return dp[0][n-1]
}
