// LeetCode 0660 - Remove 9
// https://leetcode.com/problems/remove-9/

func newInteger(n int) int {
	digits := []int{}
	for n > 0 {
		digits = append(digits, n%9)
		n /= 9
	}
	result := 0
	for i := len(digits) - 1; i >= 0; i-- {
		result = result*10 + digits[i]
	}
	return result
}
