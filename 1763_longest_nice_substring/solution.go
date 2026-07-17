// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

func longestNiceSubstring(s string) string {
	bestStart, bestLen := 0, 0
	for i := 0; i < len(s); i++ {
		lower, upper := 0, 0
		for j := i; j < len(s); j++ {
			c := s[j]
			if c >= 'a' && c <= 'z' {
				lower |= 1 << (c - 'a')
			} else {
				upper |= 1 << (c - 'A')
			}
			if lower == upper && j-i+1 > bestLen {
				bestStart = i
				bestLen = j - i + 1
			}
		}
	}
	return s[bestStart : bestStart+bestLen]
}
