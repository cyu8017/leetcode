// LeetCode 1078 - Occurrences After Bigram
// https://leetcode.com/problems/occurrences-after-bigram/

import "strings"

func findOcurrences(text string, first string, second string) []string {
	words := strings.Fields(text)
	ans := []string{}
	for i := 0; i+2 < len(words); i++ {
		if words[i] == first && words[i+1] == second {
			ans = append(ans, words[i+2])
		}
	}
	return ans
}
