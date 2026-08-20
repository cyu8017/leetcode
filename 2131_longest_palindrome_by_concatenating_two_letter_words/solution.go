// LeetCode 2131 - Longest Palindrome by Concatenating Two Letter Words
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

func longestPalindrome(words []string) int {
	freq := map[string]int{}
	for _, w := range words {
		freq[w]++
	}
	ans := 0
	center := false
	for w, c := range freq {
		rev := string([]byte{w[1], w[0]})
		if w[0] == w[1] {
			ans += (c / 2) * 4
			if c%2 == 1 {
				center = true
			}
		} else if w < rev {
			use := c
			if freq[rev] < use {
				use = freq[rev]
			}
			ans += use * 4
		}
	}
	if center {
		ans += 2
	}
	return ans
}
