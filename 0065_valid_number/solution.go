// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

func isNumber(s string) bool {
	seenDigit := false
	seenDot := false
	seenExp := false

	for i := 0; i < len(s); i++ {
		ch := s[i]

		switch {
		case ch >= '0' && ch <= '9':
			seenDigit = true
		case ch == '+' || ch == '-':
			if i > 0 && s[i-1] != 'e' && s[i-1] != 'E' {
				return false
			}
		case ch == 'e' || ch == 'E':
			if seenExp || !seenDigit {
				return false
			}
			seenExp = true
			seenDigit = false
			seenDot = false
		case ch == '.':
			if seenDot || seenExp {
				return false
			}
			seenDot = true
		default:
			return false
		}
	}

	return seenDigit
}
