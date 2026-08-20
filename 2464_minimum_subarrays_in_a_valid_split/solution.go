// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

func validSubarraySplit(nums []int) int {
	n := len(nums)
	gcd := func(a, b int) int {
		for b != 0 {
			a, b = b, a%b
		}
		return a
	}
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = 1 << 30
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		if dp[i] >= 1<<30 {
			continue
		}
		for j := i; j < n; j++ {
			if gcd(nums[i], nums[j]) > 1 {
				if dp[i]+1 < dp[j+1] {
					dp[j+1] = dp[i] + 1
				}
			}
		}
	}
	if dp[n] >= 1<<30 {
		return -1
	}
	return dp[n]
}
