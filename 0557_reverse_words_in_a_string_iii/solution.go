// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

import "strings"

func reverseWords(s string) string {
	words := strings.Split(s, " ")
	for i, word := range words {
		b := []byte(word)
		for l, r := 0, len(b)-1; l < r; l, r = l+1, r-1 {
			b[l], b[r] = b[r], b[l]
		}
		words[i] = string(b)
	}
	return strings.Join(words, " ")
}
