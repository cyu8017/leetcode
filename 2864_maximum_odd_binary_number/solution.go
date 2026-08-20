// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

func maximumOddBinaryNumber(s string) string {
	ones := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		}
	}
	zeros := len(s) - ones
	b := make([]byte, 0, len(s))
	for i := 0; i < ones-1; i++ {
		b = append(b, '1')
	}
	for i := 0; i < zeros; i++ {
		b = append(b, '0')
	}
	b = append(b, '1')
	return string(b)
}
