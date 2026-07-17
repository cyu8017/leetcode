// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

import "strings"

func truncateSentence(s string, k int) string {
	words := strings.Fields(s)
	return strings.Join(words[:k], " ")
}
