// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

import "strings"

func isPrefixOfWord(sentence string, searchWord string) int {
	words := strings.Fields(sentence)
	for i, w := range words {
		if strings.HasPrefix(w, searchWord) {
			return i + 1
		}
	}
	return -1
}
