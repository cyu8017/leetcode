// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

func toHex(num int) string {
	if num == 0 {
		return "0"
	}

	digits := "0123456789abcdef"
	value := uint32(num)
	result := make([]byte, 0, 8)

	for value > 0 {
		result = append(result, digits[value&15])
		value >>= 4
	}

	for left, right := 0, len(result)-1; left < right; left, right = left+1, right-1 {
		result[left], result[right] = result[right], result[left]
	}

	return string(result)
}
