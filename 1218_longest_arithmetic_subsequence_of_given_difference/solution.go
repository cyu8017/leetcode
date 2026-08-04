// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

func longestSubsequence(arr []int, difference int) int {
	dp := map[int]int{}
	best := 0
	for _, x := range arr {
		dp[x] = dp[x-difference] + 1
		if dp[x] > best {
			best = dp[x]
		}
	}
	return best
}
