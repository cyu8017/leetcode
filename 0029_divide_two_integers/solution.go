// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

func divide(dividend int, divisor int) int {
	if dividend == -1<<31 && divisor == -1 {
		return (1 << 31) - 1
	}
	negative := (dividend < 0) != (divisor < 0)
	if dividend < 0 {
		dividend = -dividend
	}
	if divisor < 0 {
		divisor = -divisor
	}
	quotient := 0
	for i := 31; i >= 0; i-- {
		if (dividend >> i) >= divisor {
			quotient += 1 << i
			dividend -= divisor << i
		}
	}
	if negative {
		return -quotient
	}
	return quotient
}
