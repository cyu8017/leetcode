// LeetCode 1880 - Check if Word Equals Summation of Two Words
// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

import (
	"strconv"
	"strings"
)

func wordValue(word string) int {
	var b strings.Builder
	for i := 0; i < len(word); i++ {
		b.WriteString(strconv.Itoa(int(word[i] - 'a')))
	}
	value, _ := strconv.Atoi(b.String())
	return value
}

func isSumEqual(firstWord string, secondWord string, targetWord string) bool {
	return wordValue(firstWord)+wordValue(secondWord) == wordValue(targetWord)
}
