// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

import (
	"strconv"
)

func wordsAbbreviation(words []string) []string {
	abbreviate := func(word string, prefix int) string {
		if prefix+2 >= len(word) {
			return word
		}
		middle := len(word) - prefix - 1
		candidate := word[:prefix] + strconv.Itoa(middle) + word[len(word)-1:]
		if len(candidate) < len(word) {
			return candidate
		}
		return word
	}

	prefixes := make([]int, len(words))
	for index := range prefixes {
		prefixes[index] = 1
	}

	changed := true
	for changed {
		changed = false
		groups := make(map[string][]int)
		for index, word := range words {
			key := abbreviate(word, prefixes[index])
			groups[key] = append(groups[key], index)
		}
		for _, indices := range groups {
			if len(indices) > 1 {
				changed = true
				for _, index := range indices {
					prefixes[index]++
				}
			}
		}
	}

	result := make([]string, len(words))
	for index, word := range words {
		result[index] = abbreviate(word, prefixes[index])
	}
	return result
}
