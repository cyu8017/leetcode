// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

func convertToBase7(num int) string {
	if num == 0 {
		return "0"
	}
	negative := num < 0
	if negative {
		num = -num
	}
	digits := make([]byte, 0)
	for num > 0 {
		digits = append(digits, byte('0'+num%7))
		num /= 7
	}
	for left, right := 0, len(digits)-1; left < right; left, right = left+1, right-1 {
		digits[left], digits[right] = digits[right], digits[left]
	}
	result := string(digits)
	if negative {
		return "-" + result
	}
	return result
}
