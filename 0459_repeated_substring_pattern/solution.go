// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

import "strings"

func repeatedSubstringPattern(s string) bool {
	doubled := s + s
	return strings.Contains(doubled[1:len(doubled)-1], s)
}
