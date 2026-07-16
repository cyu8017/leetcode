// LeetCode 0288 - Unique Word Abbreviation
// https://leetcode.com/problems/unique-word-abbreviation/

import "fmt"

type ValidWordAbbr struct {
	groups map[string]map[string]struct{}
}

func Constructor(dictionary []string) ValidWordAbbr {
	obj := ValidWordAbbr{groups: make(map[string]map[string]struct{})}
	for _, word := range dictionary {
		key := abbreviate(word)
		if obj.groups[key] == nil {
			obj.groups[key] = make(map[string]struct{})
		}
		obj.groups[key][word] = struct{}{}
	}
	return obj
}

func (this *ValidWordAbbr) IsUnique(word string) bool {
	key := abbreviate(word)
	words, ok := this.groups[key]
	if !ok {
		return true
	}
	_, contains := words[word]
	return len(words) == 1 && contains
}

func abbreviate(word string) string {
	if len(word) <= 2 {
		return word
	}
	return fmt.Sprintf("%c%d%c", word[0], len(word)-2, word[len(word)-1])
}
