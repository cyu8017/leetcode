// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

func longestSubsequence(s string, k int) int {
	zeros := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
		}
	}
	val := 0
	ones := 0
	pow := 1
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '1' {
			if pow > k || val+pow > k {
				continue
			}
			val += pow
			ones++
		}
		if pow <= k {
			pow <<= 1
		}
	}
	return zeros + ones
}
