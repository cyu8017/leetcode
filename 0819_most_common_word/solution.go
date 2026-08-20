// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

import "unicode"

func mostCommonWord(paragraph string, banned []string) string {
	bannedSet := map[string]bool{}
	for _, w := range banned {
		bannedSet[w] = true
	}
	counts := map[string]int{}
	var word []byte
	flush := func() {
		if len(word) == 0 {
			return
		}
		s := string(word)
		word = word[:0]
		if !bannedSet[s] {
			counts[s]++
		}
	}
	for i := 0; i < len(paragraph); i++ {
		ch := rune(paragraph[i])
		if unicode.IsLetter(ch) {
			word = append(word, byte(unicode.ToLower(ch)))
		} else {
			flush()
		}
	}
	flush()
	best, ans := -1, ""
	for w, c := range counts {
		if c > best {
			best, ans = c, w
		}
	}
	return ans
}
