// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

func reformat(s string) string {
	var letters, digits []byte
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			digits = append(digits, s[i])
		} else {
			letters = append(letters, s[i])
		}
	}
	diff := len(letters) - len(digits)
	if diff < 0 {
		diff = -diff
	}
	if diff > 1 {
		return ""
	}
	if len(digits) > len(letters) {
		letters, digits = digits, letters
	}
	answer := make([]byte, 0, len(s))
	for i, char := range letters {
		answer = append(answer, char)
		if i < len(digits) {
			answer = append(answer, digits[i])
		}
	}
	return string(answer)
}
