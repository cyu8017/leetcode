// LeetCode 1967 - Number of Strings That Appear as Substrings in Word
// https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

import "strings"

func numOfStrings(patterns []string, word string) int {
	ans := 0
	for _, p := range patterns {
		if strings.Contains(word, p) {
			ans++
		}
	}
	return ans
}
