// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

import (
	"strings"
	"unicode"
)

func maskPII(s string) string {
	if strings.Contains(s, "@") {
		parts := strings.Split(strings.ToLower(s), "@")
		name, domain := parts[0], parts[1]
		return string(name[0]) + "*****" + string(name[len(name)-1]) + "@" + domain
	}
	digits := []byte{}
	for i := 0; i < len(s); i++ {
		if unicode.IsDigit(rune(s[i])) {
			digits = append(digits, s[i])
		}
	}
	local := string(digits[len(digits)-4:])
	country := len(digits) - 10
	if country == 0 {
		return "***-***-" + local
	}
	return "+" + strings.Repeat("*", country) + "-***-***-" + local
}
