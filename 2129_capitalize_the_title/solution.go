// LeetCode 2129 - Capitalize the Title
// https://leetcode.com/problems/capitalize-the-title/

import "strings"

func capitalizeTitle(title string) string {
	words := strings.Fields(title)
	for i, w := range words {
		w = strings.ToLower(w)
		if len(w) > 2 {
			w = strings.ToUpper(w[:1]) + w[1:]
		}
		words[i] = w
	}
	return strings.Join(words, " ")
}
