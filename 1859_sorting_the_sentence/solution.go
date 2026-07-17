// LeetCode 1859 - Sorting the Sentence
// https://leetcode.com/problems/sorting-the-sentence/

import "strings"

func sortSentence(s string) string {
	tokens := strings.Fields(s)
	ordered := make([]string, len(tokens))

	for _, token := range tokens {
		position := int(token[len(token)-1] - '0')
		ordered[position-1] = token[:len(token)-1]
	}

	return strings.Join(ordered, " ")
}
