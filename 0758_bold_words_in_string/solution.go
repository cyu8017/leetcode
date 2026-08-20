// LeetCode 0758 - Bold Words in String
// https://leetcode.com/problems/bold-words-in-string/

import "strings"

func boldWords(words []string, s string) string {
	n := len(s)
	bold := make([]bool, n)
	for _, word := range words {
		start := strings.Index(s, word)
		for start != -1 {
			for i := start; i < start+len(word); i++ {
				bold[i] = true
			}
			next := strings.Index(s[start+1:], word)
			if next == -1 {
				break
			}
			start = start + 1 + next
		}
	}
	parts := []string{}
	i := 0
	for i < n {
		if bold[i] {
			parts = append(parts, "<b>")
			for i < n && bold[i] {
				parts = append(parts, string(s[i]))
				i++
			}
			parts = append(parts, "</b>")
		} else {
			parts = append(parts, string(s[i]))
			i++
		}
	}
	out := strings.Join(parts, "")
	out = strings.ReplaceAll(out, "<b>", "**")
	out = strings.ReplaceAll(out, "</b>", "**")
	return out
}
