// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

import (
	"strings"
	"unicode"
)

func findWords(words []string) []string {
	rows := []map[rune]bool{
		toSet("qwertyuiop"),
		toSet("asdfghjkl"),
		toSet("zxcvbnm"),
	}
	result := make([]string, 0)
	for _, word := range words {
		letters := map[rune]bool{}
		for _, ch := range word {
			if unicode.IsLetter(ch) {
				letters[unicode.ToLower(ch)] = true
			}
		}
		for _, row := range rows {
			subset := true
			for letter := range letters {
				if !row[letter] {
					subset = false
					break
				}
			}
			if subset {
				result = append(result, word)
				break
			}
		}
	}
	return result
}

func toSet(text string) map[rune]bool {
	set := map[rune]bool{}
	for _, ch := range strings.ToLower(text) {
		set[ch] = true
	}
	return set
}
