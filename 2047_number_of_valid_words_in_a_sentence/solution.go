// LeetCode 2047 - Number of Valid Words in a Sentence
// https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

import "strings"

func countValidWords(sentence string) int {
	valid := func(w string) bool {
		if len(w) == 0 {
			return false
		}
		hyphen := 0
		for i := 0; i < len(w); i++ {
			c := w[i]
			if c >= '0' && c <= '9' {
				return false
			}
			if c == '-' {
				hyphen++
				if hyphen > 1 || i == 0 || i == len(w)-1 {
					return false
				}
				if w[i-1] < 'a' || w[i-1] > 'z' || w[i+1] < 'a' || w[i+1] > 'z' {
					return false
				}
			} else if c == '!' || c == '.' || c == ',' {
				if i != len(w)-1 {
					return false
				}
			} else if c < 'a' || c > 'z' {
				return false
			}
		}
		return true
	}
	ans := 0
	for _, w := range strings.Fields(sentence) {
		if valid(w) {
			ans++
		}
	}
	return ans
}
