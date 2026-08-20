// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

import (
	"sort"
	"strings"
)

type AutocompleteSystem struct {
	counts  map[string]int
	current string
}

func Constructor(sentences []string, times []int) AutocompleteSystem {
	counts := map[string]int{}
	for i, sentence := range sentences {
		counts[sentence] += times[i]
	}
	return AutocompleteSystem{counts: counts}
}

func (a *AutocompleteSystem) Input(c byte) []string {
	if c == '#' {
		a.counts[a.current]++
		a.current = ""
		return []string{}
	}
	a.current += string(c)
	matches := []string{}
	for sentence := range a.counts {
		if strings.HasPrefix(sentence, a.current) {
			matches = append(matches, sentence)
		}
	}
	sort.Slice(matches, func(i, j int) bool {
		if a.counts[matches[i]] == a.counts[matches[j]] {
			return matches[i] < matches[j]
		}
		return a.counts[matches[i]] > a.counts[matches[j]]
	})
	if len(matches) > 3 {
		matches = matches[:3]
	}
	return matches
}
