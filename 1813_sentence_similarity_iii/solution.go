// LeetCode 1813 - Sentence Similarity III
// https://leetcode.com/problems/sentence-similarity-iii/

import "strings"

func areSentencesSimilar(sentence1 string, sentence2 string) bool {
	words1 := strings.Fields(sentence1)
	words2 := strings.Fields(sentence2)
	n1, n2 := len(words1), len(words2)

	i := 0
	for i < n1 && i < n2 && words1[i] == words2[i] {
		i++
	}
	if i == n1 || i == n2 {
		return true
	}

	j1, j2 := n1-1, n2-1
	for j1 >= i && j2 >= i && words1[j1] == words2[j2] {
		j1--
		j2--
	}
	return j1 < i || j2 < i
}
