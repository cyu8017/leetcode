// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

import "strings"

func stringMatching(words []string) []string {
	var answer []string
	for i, word := range words {
		for j, other := range words {
			if i != j && strings.Contains(other, word) {
				answer = append(answer, word)
				break
			}
		}
	}
	return answer
}
