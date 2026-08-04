// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

func maximum69Number(num int) int {
	chars := []byte{}
	n := num
	if n == 0 {
		chars = []byte{'0'}
	} else {
		for n > 0 {
			chars = append([]byte{byte('0' + n%10)}, chars...)
			n /= 10
		}
	}
	for i := range chars {
		if chars[i] == '6' {
			chars[i] = '9'
			break
		}
	}
	res := 0
	for _, c := range chars {
		res = res*10 + int(c-'0')
	}
	return res
}
