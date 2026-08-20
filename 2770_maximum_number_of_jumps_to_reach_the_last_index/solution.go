// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

func maximumJumps(nums []int, target int) int {
	n := len(nums)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 0
	for i := 0; i < n; i++ {
		if dp[i] < 0 {
			continue
		}
		for j := i + 1; j < n; j++ {
			diff := nums[j] - nums[i]
			if diff < 0 {
				diff = -diff
			}
			if diff <= target {
				if dp[i]+1 > dp[j] {
					dp[j] = dp[i] + 1
				}
			}
		}
	}
	return dp[n-1]
}
