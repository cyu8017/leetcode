// LeetCode 0686 - Repeated String Match
// https://leetcode.com/problems/repeated-string-match/

import "strings"

func repeatedStringMatch(a string, b string) int {
	repeats := (len(b) + len(a) - 1) / len(a)
	built := strings.Repeat(a, repeats)
	if strings.Contains(built, b) {
		return repeats
	}
	if strings.Contains(built+a, b) {
		return repeats + 1
	}
	return -1
}
