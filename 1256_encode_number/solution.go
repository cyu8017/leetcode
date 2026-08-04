// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

func encode(num int) string {
	num++
	bits := ""
	for num > 0 {
		bits = string('0'+byte(num%2)) + bits
		num /= 2
	}
	if len(bits) <= 1 {
		return ""
	}
	return bits[1:]
}
