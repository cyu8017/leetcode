// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

import "strings"

func toGoatLatin(sentence string) string {
	vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true}
	words := strings.Fields(sentence)
	out := make([]string, len(words))
	for i, word := range words {
		var goat string
		if vowels[word[0]] {
			goat = word + "ma"
		} else {
			goat = word[1:] + string(word[0]) + "ma"
		}
		out[i] = goat + strings.Repeat("a", i+1)
	}
	return strings.Join(out, " ")
}
