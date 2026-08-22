// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

import "strings"

func hasMatch(s string, p string) bool {
	i := strings.IndexByte(p, '*')
	left, right := p[:i], p[i+1:]
	li := strings.Index(s, left)
	if li < 0 {
		return false
	}
	return strings.Contains(s[li+len(left):], right)
}
