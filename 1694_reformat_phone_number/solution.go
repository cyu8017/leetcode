// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

import "strings"

func reformatNumber(number string) string {
	var b strings.Builder
	for i := 0; i < len(number); i++ {
		c := number[i]
		if c >= '0' && c <= '9' {
			b.WriteByte(c)
		}
	}
	s := b.String()
	out := []string{}
	for len(s) > 4 {
		out = append(out, s[:3])
		s = s[3:]
	}
	if len(s) == 4 {
		out = append(out, s[:2], s[2:])
	} else if len(s) > 0 {
		out = append(out, s)
	}
	return strings.Join(out, "-")
}
