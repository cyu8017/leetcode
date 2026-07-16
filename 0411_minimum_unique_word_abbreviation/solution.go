// LeetCode 0411 - Minimum Unique Word Abbreviation
// https://leetcode.com/problems/minimum-unique-word-abbreviation/

import (
	"strconv"
	"strings"
)

func minAbbreviation(target string, dictionary []string) string {
	words := make([]string, 0)
	for _, word := range dictionary {
		if len(word) == len(target) {
			words = append(words, word)
		}
	}

	bestLen := len(target) + 1
	result := target

	matches := func(word, abbr string) bool {
		index := 0
		pointer := 0
		for index < len(word) && pointer < len(abbr) {
			if abbr[pointer] >= '0' && abbr[pointer] <= '9' {
				if abbr[pointer] == '0' {
					return false
				}
				number := 0
				for pointer < len(abbr) && abbr[pointer] >= '0' && abbr[pointer] <= '9' {
					number = number*10 + int(abbr[pointer]-'0')
					pointer++
				}
				index += number
			} else {
				if index >= len(word) || word[index] != abbr[pointer] {
					return false
				}
				index++
				pointer++
			}
		}
		return index == len(word) && pointer == len(abbr)
	}

	valid := func(abbr string) bool {
		if !matches(target, abbr) {
			return false
		}
		for _, word := range words {
			if matches(word, abbr) {
				return false
			}
		}
		return true
	}

	var dfs func(index int, parts []string, skip int)
	dfs = func(index int, parts []string, skip int) {
		if index == len(target) {
			abbr := strings.Join(parts, "")
			if skip > 0 {
				abbr += strconv.Itoa(skip)
			}
			if valid(abbr) {
				if len(abbr) < bestLen || (len(abbr) == bestLen && abbr < result) {
					bestLen = len(abbr)
					result = abbr
				}
			}
			return
		}

		dfs(index+1, parts, skip+1)

		newParts := append([]string{}, parts...)
		if skip > 0 {
			newParts = append(newParts, strconv.Itoa(skip))
		}
		newParts = append(newParts, string(target[index]))
		dfs(index+1, newParts, 0)
	}

	dfs(0, []string{}, 0)
	return result
}
