// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

func longestPalindrome(s string) string {
	bestStart := 0
	bestLen := 0
	bytes := []byte(s)

	expand := func(left, right int) {
		for left >= 0 && right < len(bytes) && bytes[left] == bytes[right] {
			left--
			right++
		}
		length := right - left - 1
		if length > bestLen {
			bestLen = length
			bestStart = left + 1
		}
	}

	for i := 0; i < len(bytes); i++ {
		expand(i, i)
		expand(i, i+1)
	}

	return string(bytes[bestStart : bestStart+bestLen])
}
