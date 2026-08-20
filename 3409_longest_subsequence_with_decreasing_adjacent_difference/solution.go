// LeetCode 3409 - Longest Subsequence With Decreasing Adjacent Difference
// https://leetcode.com/problems/longest-subsequence-with-decreasing-adjacent-difference/

func longestSubsequence(nums []int) int {
	n := len(nums)
	ans := 1
	// dp[i][d] = longest ending at i with last diff d
	dp := make([][]int, n)
	for i := range dp {
		dp[i] = make([]int, 301)
	}
	for i := 0; i < n; i++ {
		for j := 0; j < i; j++ {
			d := nums[i] - nums[j]
			if d < 0 {
				d = -d
			}
			best := 1
			for pd := d; pd <= 300; pd++ {
				if dp[j][pd] > best {
					best = dp[j][pd]
				}
			}
			if best+1 > dp[i][d] {
				dp[i][d] = best + 1
			}
			if dp[i][d] > ans {
				ans = dp[i][d]
			}
		}
		if dp[i][0] < 1 {
			dp[i][0] = 1
		}
	}
	return ans
}
