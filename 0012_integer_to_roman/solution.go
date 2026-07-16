// LeetCode 0012 - Integer to Roman
// https://leetcode.com/problems/integer-to-roman/

func intToRoman(num int) string {
	values := []int{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1}
	symbols := []string{"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"}
	result := make([]byte, 0, 15)

	for i, value := range values {
		for num >= value {
			result = append(result, symbols[i]...)
			num -= value
		}
	}

	return string(result)
}
