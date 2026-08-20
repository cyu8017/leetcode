// LeetCode 2042 - Check if Numbers Are Ascending in a Sentence
// https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

import "strconv"
import "strings"

func areNumbersAscending(s string) bool {
	prev := -1
	for _, tok := range strings.Fields(s) {
		if tok[0] >= '0' && tok[0] <= '9' {
			v, _ := strconv.Atoi(tok)
			if v <= prev {
				return false
			}
			prev = v
		}
	}
	return true
}
