// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

func greatestLetter(s string) string {
	var lower, upper [26]bool
	for i := 0; i < len(s); i++ {
		c := s[i]
		if c >= 'a' && c <= 'z' {
			lower[c-'a'] = true
		} else {
			upper[c-'A'] = true
		}
	}
	for i := 25; i >= 0; i-- {
		if lower[i] && upper[i] {
			return string(byte('A' + i))
		}
	}
	return ""
}
