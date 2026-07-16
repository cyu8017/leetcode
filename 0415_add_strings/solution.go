// LeetCode 0415 - Add Strings
// https://leetcode.com/problems/add-strings/

func addStrings(num1 string, num2 string) string {
	index1 := len(num1) - 1
	index2 := len(num2) - 1
	carry := 0
	digits := make([]byte, 0)

	for index1 >= 0 || index2 >= 0 || carry > 0 {
		if index1 >= 0 {
			carry += int(num1[index1] - '0')
			index1--
		}
		if index2 >= 0 {
			carry += int(num2[index2] - '0')
			index2--
		}
		digits = append(digits, byte('0'+carry%10))
		carry /= 10
	}

	for left, right := 0, len(digits)-1; left < right; left, right = left+1, right-1 {
		digits[left], digits[right] = digits[right], digits[left]
	}
	return string(digits)
}
