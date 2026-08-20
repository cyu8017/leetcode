// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

import "strings"

func spellchecker(wordlist []string, queries []string) []string {
	isVowel := func(c byte) bool {
		switch c {
		case 'a', 'e', 'i', 'o', 'u':
			return true
		}
		return false
	}
	devowel := func(w string) string {
		b := []byte(strings.ToLower(w))
		for i, c := range b {
			if isVowel(c) {
				b[i] = '*'
			}
		}
		return string(b)
	}
	exact := map[string]bool{}
	lower := map[string]string{}
	vowelMap := map[string]string{}
	for _, w := range wordlist {
		exact[w] = true
		low := strings.ToLower(w)
		if _, ok := lower[low]; !ok {
			lower[low] = w
		}
		dv := devowel(w)
		if _, ok := vowelMap[dv]; !ok {
			vowelMap[dv] = w
		}
	}
	ans := make([]string, len(queries))
	for i, q := range queries {
		if exact[q] {
			ans[i] = q
		} else if w, ok := lower[strings.ToLower(q)]; ok {
			ans[i] = w
		} else if w, ok := vowelMap[devowel(q)]; ok {
			ans[i] = w
		} else {
			ans[i] = ""
		}
	}
	return ans
}
