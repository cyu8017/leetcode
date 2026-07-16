// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

import "strings"

func wordPattern(pattern string, s string) bool {
	words := strings.Fields(s)
	if len(pattern) != len(words) {
		return false
	}

	charToWord := make(map[byte]string)
	wordToChar := make(map[string]byte)
	for index := 0; index < len(pattern); index++ {
		ch := pattern[index]
		word := words[index]
		if mapped, ok := charToWord[ch]; ok {
			if mapped != word {
				return false
			}
		} else {
			if _, ok := wordToChar[word]; ok {
				return false
			}
			charToWord[ch] = word
			wordToChar[word] = ch
		}
	}
	return true
}
