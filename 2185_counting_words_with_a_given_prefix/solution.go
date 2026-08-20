// LeetCode 2185 - Counting Words With a Given Prefix
// https://leetcode.com/problems/counting-words-with-a-given-prefix/

import "strings"

func prefixCount(words []string, pref string) int {
	ans := 0
	for _, w := range words {
		if strings.HasPrefix(w, pref) {
			ans++
		}
	}
	return ans
}
