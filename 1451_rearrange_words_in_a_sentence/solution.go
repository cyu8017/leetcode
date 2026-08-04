// LeetCode 1451 - Rearrange Words in a Sentence
// https://leetcode.com/problems/rearrange-words-in-a-sentence/

import (
	"sort"
	"strings"
)

func arrangeWords(text string) string {
	words := strings.Fields(strings.ToLower(text))
	sort.SliceStable(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	s := strings.Join(words, " ")
	if len(s) == 0 {
		return s
	}
	return strings.ToUpper(s[:1]) + s[1:]
}
