// LeetCode 0884 - Uncommon Words from Two Sentences
// https://leetcode.com/problems/uncommon-words-from-two-sentences/

import "strings"

func uncommonFromSentences(s1 string, s2 string) []string {
	count := map[string]int{}
	for _, w := range strings.Fields(s1 + " " + s2) {
		count[w]++
	}
	ans := []string{}
	for w, c := range count {
		if c == 1 {
			ans = append(ans, w)
		}
	}
	return ans
}
