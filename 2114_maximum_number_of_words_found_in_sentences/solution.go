// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

import "strings"

func mostWordsFound(sentences []string) int {
	ans := 0
	for _, s := range sentences {
		c := strings.Count(s, " ") + 1
		if c > ans {
			ans = c
		}
	}
	return ans
}
