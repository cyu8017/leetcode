// LeetCode 1324 - Print Words Vertically
// https://leetcode.com/problems/print-words-vertically/

import "strings"

func printVertically(s string) []string {
	words := strings.Fields(s)
	maxLen := 0
	for _, w := range words {
		if len(w) > maxLen {
			maxLen = len(w)
		}
	}
	answer := make([]string, maxLen)
	for i := 0; i < maxLen; i++ {
		var b strings.Builder
		for _, w := range words {
			if i < len(w) {
				b.WriteByte(w[i])
			} else {
				b.WriteByte(' ')
			}
		}
		answer[i] = strings.TrimRight(b.String(), " ")
	}
	return answer
}
