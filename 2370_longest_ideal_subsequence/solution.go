// LeetCode 2370 - Longest Ideal Subsequence
// https://leetcode.com/problems/longest-ideal-subsequence/

func longestIdealString(s string, k int) int {
	dp := make([]int, 26)
	ans := 0
	for i := 0; i < len(s); i++ {
		c := int(s[i] - 'a')
		best := 0
		for p := 0; p < 26; p++ {
			diff := c - p
			if diff < 0 {
				diff = -diff
			}
			if diff <= k && dp[p] > best {
				best = dp[p]
			}
		}
		dp[c] = best + 1
		if dp[c] > ans {
			ans = dp[c]
		}
	}
	return ans
}
