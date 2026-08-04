// LeetCode 1271 - Hexspeak
// https://leetcode.com/problems/hexspeak/

import "strconv"

func toHexspeak(num string) string {
	value, _ := strconv.ParseInt(num, 10, 64)
	digits := "0123456789ABCDEF"
	out := ""
	if value == 0 {
		return "O"
	}
	for value > 0 {
		rem := value % 16
		if rem >= 2 && rem <= 9 {
			return "ERROR"
		}
		out = string(digits[rem]) + out
		value /= 16
	}
	b := []byte(out)
	for i := range b {
		if b[i] == '0' {
			b[i] = 'O'
		} else if b[i] == '1' {
			b[i] = 'I'
		}
	}
	return string(b)
}
