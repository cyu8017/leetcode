// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

func removePalindromeSub(s string) int {
	if len(s) == 0 {
		return 0
	}
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return 2
		}
	}
	return 1
}
