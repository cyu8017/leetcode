// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

import "strings"

func replaceWords(dictionary []string, sentence string) string {
	roots := map[string]struct{}{}
	for _, root := range dictionary {
		roots[root] = struct{}{}
	}
	replace := func(word string) string {
		for i := 1; i <= len(word); i++ {
			prefix := word[:i]
			if _, ok := roots[prefix]; ok {
				return prefix
			}
		}
		return word
	}
	words := strings.Fields(sentence)
	for i, word := range words {
		words[i] = replace(word)
	}
	return strings.Join(words, " ")
}
