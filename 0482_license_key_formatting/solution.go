// LeetCode 0482 - License Key Formatting
// https://leetcode.com/problems/license-key-formatting/

import (
	"strings"
	"unicode"
)

func licenseKeyFormatting(s string, k int) string {
	var chars []rune
	for _, ch := range s {
		if ch != '-' {
			chars = append(chars, unicode.ToUpper(ch))
		}
	}
	if len(chars) == 0 {
		return ""
	}
	firstLen := len(chars) % k
	if firstLen == 0 {
		firstLen = k
	}
	parts := []string{string(chars[:firstLen])}
	for index := firstLen; index < len(chars); index += k {
		parts = append(parts, string(chars[index:index+k]))
	}
	return strings.Join(parts, "-")
}
