// LeetCode 1668 - Maximum Repeating Substring
// https://leetcode.com/problems/maximum-repeating-substring/

import "strings"

func maxRepeating(sequence, word string) int {
	k := 0
	for strings.Contains(sequence, strings.Repeat(word, k+1)) {
		k++
	}
	return k
}
