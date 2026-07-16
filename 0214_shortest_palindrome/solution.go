// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

func shortestPalindrome(s string) string {
	if s == "" {
		return ""
	}
	reversed := reverseString(s)
	combined := s + "#" + reversed
	pi := make([]int, len(combined))
	lps := 0
	for i := 1; i < len(combined); i++ {
		for lps > 0 && combined[i] != combined[lps] {
			lps = pi[lps-1]
		}
		if combined[i] == combined[lps] {
			lps++
		}
		pi[i] = lps
	}
	prefixLen := pi[len(combined)-1]
	return reversed[:len(s)-prefixLen] + s
}

func reverseString(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
