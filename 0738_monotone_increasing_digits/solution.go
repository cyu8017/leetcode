// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

import "strconv"

func monotoneIncreasingDigits(n int) int {
	digits := []byte(strconv.Itoa(n))
	mark := len(digits)
	for i := len(digits) - 1; i > 0; i-- {
		if digits[i] < digits[i-1] {
			digits[i-1]--
			mark = i
		}
	}
	for i := mark; i < len(digits); i++ {
		digits[i] = '9'
	}
	v, _ := strconv.Atoi(string(digits))
	return v
}
