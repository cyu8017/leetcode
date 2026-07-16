// LeetCode 0400 - Nth Digit
// https://leetcode.com/problems/nth-digit/

import "strconv"

func findNthDigit(n int) int {
	digits := 1
	count := int64(9)
	start := int64(1)

	for n > digits*int(count) {
		n -= digits * int(count)
		digits++
		count *= 10
		start *= 10
	}

	number := start + int64(n-1)/int64(digits)
	text := strconv.FormatInt(number, 10)
	return int(text[(n-1)%digits] - '0')
}
