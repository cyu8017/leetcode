// LeetCode 0520 - Detect Capital
// https://leetcode.com/problems/detect-capital/

import "unicode"

func detectCapitalUse(word string) bool {
	allUpper := true
	allLower := true
	for _, ch := range word {
		if unicode.IsUpper(ch) {
			allLower = false
		} else {
			allUpper = false
		}
	}
	if allUpper || allLower {
		return true
	}
	runes := []rune(word)
	for _, ch := range runes[1:] {
		if unicode.IsUpper(ch) {
			return false
		}
	}
	return unicode.IsUpper(runes[0])
}
