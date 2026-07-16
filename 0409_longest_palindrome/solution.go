// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

func longestPalindrome(s string) int {
	counts := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}

	length := 0
	hasOdd := false
	for _, count := range counts {
		length += (count / 2) * 2
		if count%2 == 1 {
			hasOdd = true
		}
	}

	if hasOdd {
		return length + 1
	}
	return length
}
