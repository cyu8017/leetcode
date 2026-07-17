// LeetCode 1704 - Determine if String Halves Are Alike
// https://leetcode.com/problems/determine-if-string-halves-are-alike/

import "strings"

func halvesAreAlike(s string) bool {
	const vowels = "aeiouAEIOU"
	mid := len(s) / 2
	balance := 0
	for i := 0; i < len(s); i++ {
		if strings.IndexByte(vowels, s[i]) >= 0 {
			if i < mid {
				balance++
			} else {
				balance--
			}
		}
	}
	return balance == 0
}
