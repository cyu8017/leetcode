// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

func makePalindrome(s string) bool {
	diff := 0
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			diff++
			if diff > 2 {
				return false
			}
		}
	}
	return true
}
