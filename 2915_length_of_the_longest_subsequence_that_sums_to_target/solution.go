// LeetCode 2915 - Length of the Longest Subsequence That Sums to Target
// https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/

func lengthOfLongestSubsequence(nums []int, target int) int {
	dp := make([]int, target+1)
	for i := range dp {
		dp[i] = -1
	}
	dp[0] = 0
	for _, v := range nums {
		for s := target; s >= v; s-- {
			if dp[s-v] >= 0 && dp[s-v]+1 > dp[s] {
				dp[s] = dp[s-v] + 1
			}
		}
	}
	return dp[target]
}
