// LeetCode 0616 - Add Bold Tag in String
// https://leetcode.com/problems/add-bold-tag-in-string/

import "strings"

func addBoldTag(s string, words []string) string {
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
	var b strings.Builder
	i := 0
	for i < n {
		if bold[i] {
			b.WriteString("<b>")
			for i < n && bold[i] {
				b.WriteByte(s[i])
				i++
			}
			b.WriteString("</b>")
		} else {
			b.WriteByte(s[i])
			i++
		}
	}
	return b.String()
}
