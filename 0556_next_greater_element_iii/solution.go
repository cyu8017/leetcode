// LeetCode 0556 - Next Greater Element III
// https://leetcode.com/problems/next-greater-element-iii/

import "strconv"

func nextGreaterElement(n int) int {
	digits := []byte(strconv.Itoa(n))
	i := len(digits) - 2
	for i >= 0 && digits[i] >= digits[i+1] {
		i--
	}
	if i < 0 {
		return -1
	}
	j := len(digits) - 1
	for digits[j] <= digits[i] {
		j--
	}
	digits[i], digits[j] = digits[j], digits[i]
	for l, r := i+1, len(digits)-1; l < r; l, r = l+1, r-1 {
		digits[l], digits[r] = digits[r], digits[l]
	}
	value, err := strconv.Atoi(string(digits))
	if err != nil || value > 1<<31-1 {
		return -1
	}
	return value
}
