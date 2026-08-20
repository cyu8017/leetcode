// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

func smallestNumber(n int) string {
	if n == 0 {
		return "0"
	}
	if n == 1 {
		return "1"
	}
	digits := []byte{}
	for d := 9; d >= 2; d-- {
		for n%d == 0 {
			digits = append(digits, byte('0'+d))
			n /= d
		}
	}
	if n > 1 {
		return "-1"
	}
	for i, j := 0, len(digits)-1; i < j; i, j = i+1, j-1 {
		digits[i], digits[j] = digits[j], digits[i]
	}
	return string(digits)
}
