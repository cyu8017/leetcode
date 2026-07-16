// LeetCode 0291 - Word Pattern II
// https://leetcode.com/problems/word-pattern-ii/

func wordPatternMatch(pattern string, s string) bool {
	var backtrack func(patternIndex int, stringIndex int) bool
	charToWord := make(map[byte]string)
	wordToChar := make(map[string]byte)

	backtrack = func(patternIndex int, stringIndex int) bool {
		if patternIndex == len(pattern) {
			return stringIndex == len(s)
		}

		ch := pattern[patternIndex]
		if word, ok := charToWord[ch]; ok {
			if !hasPrefixAt(s, word, stringIndex) {
				return false
			}
			return backtrack(patternIndex+1, stringIndex+len(word))
		}

		for end := stringIndex + 1; end <= len(s); end++ {
			word := s[stringIndex:end]
			if _, ok := wordToChar[word]; ok {
				continue
			}
			charToWord[ch] = word
			wordToChar[word] = ch
			if backtrack(patternIndex+1, end) {
				return true
			}
			delete(charToWord, ch)
			delete(wordToChar, word)
		}
		return false
	}

	return backtrack(0, 0)
}

func hasPrefixAt(text, prefix string, start int) bool {
	if start+len(prefix) > len(text) {
		return false
	}
	return text[start:start+len(prefix)] == prefix
}
