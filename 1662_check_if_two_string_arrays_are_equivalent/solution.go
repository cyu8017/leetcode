// LeetCode 1662 - Check If Two String Arrays are Equivalent
// https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

import "strings"

func arrayStringsAreEqual(word1, word2 []string) bool {
	return strings.Join(word1, "") == strings.Join(word2, "")
}
