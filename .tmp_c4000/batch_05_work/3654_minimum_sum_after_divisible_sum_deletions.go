// LeetCode 3654 - Minimum Sum After Divisible Sum Deletions
// https://leetcode.com/problems/minimum-sum-after-divisible-sum-deletions/

func minArraySum(nums []int, k int) int64 {
	n := len(nums)
	prefix := make([]int, n+1)
	for i, v := range nums {
		prefix[i+1] = (prefix[i] + v) % k
	}
	const inf int64 = 1 << 62
	dp := make([]int64, n+1)
	best := make([]int64, k)
	for i := range best {
		best[i] = inf
	}
	best[0] = 0
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + int64(nums[i-1])
		if best[prefix[i]] < dp[i] {
			dp[i] = best[prefix[i]]
		}
		if dp[i] < best[prefix[i]] {
			best[prefix[i]] = dp[i]
		}
	}
	return dp[n]
}
