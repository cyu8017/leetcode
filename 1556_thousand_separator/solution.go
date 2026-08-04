// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

import "strconv"
import "strings"

func thousandSeparator(n int) string {
	s := strconv.Itoa(n)
	parts := []string{}
	for len(s) > 0 {
		start := len(s) - 3
		if start < 0 {
			start = 0
		}
		parts = append(parts, s[start:])
		s = s[:start]
	}
	for i, j := 0, len(parts)-1; i < j; i, j = i+1, j-1 {
		parts[i], parts[j] = parts[j], parts[i]
	}
	return strings.Join(parts, ".")
}
