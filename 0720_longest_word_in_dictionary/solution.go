// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

import "sort"

func longestWord(words []string) string {
	sort.Strings(words)
	built := map[string]bool{"": true}
	best := ""
	for _, word := range words {
		if built[word[:len(word)-1]] {
			built[word] = true
			if len(word) > len(best) {
				best = word
			}
		}
	}
	return best
}
