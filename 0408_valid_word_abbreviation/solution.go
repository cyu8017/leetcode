// LeetCode 0408 - Valid Word Abbreviation
// https://leetcode.com/problems/valid-word-abbreviation/

func validWordAbbreviation(word string, abbr string) bool {
	wordIndex := 0
	abbrIndex := 0

	for wordIndex < len(word) && abbrIndex < len(abbr) {
		if abbr[abbrIndex] >= '0' && abbr[abbrIndex] <= '9' {
			if abbr[abbrIndex] == '0' {
				return false
			}

			number := 0
			for abbrIndex < len(abbr) && abbr[abbrIndex] >= '0' && abbr[abbrIndex] <= '9' {
				number = number*10 + int(abbr[abbrIndex]-'0')
				abbrIndex++
			}
			wordIndex += number
		} else {
			if word[wordIndex] != abbr[abbrIndex] {
				return false
			}
			wordIndex++
			abbrIndex++
		}
	}

	return wordIndex == len(word) && abbrIndex == len(abbr)
}
