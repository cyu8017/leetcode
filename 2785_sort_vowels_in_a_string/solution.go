// LeetCode 2785 - Sort Vowels in a String
// https://leetcode.com/problems/sort-vowels-in-a-string/

import "sort"

func sortVowels(s string) string {
	isVowel := func(c byte) bool {
		switch c {
		case 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U':
			return true
		}
		return false
	}
	vowels := []byte{}
	for i := 0; i < len(s); i++ {
		if isVowel(s[i]) {
			vowels = append(vowels, s[i])
		}
	}
	sort.Slice(vowels, func(i, j int) bool { return vowels[i] < vowels[j] })
	b := []byte(s)
	vi := 0
	for i := range b {
		if isVowel(b[i]) {
			b[i] = vowels[vi]
			vi++
		}
	}
	return string(b)
}
