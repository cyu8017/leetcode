// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

func confusingNumber(n int) bool {
	rotate := map[byte]byte{'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
	s := []byte{}
	for x := n; x > 0; x /= 10 {
		s = append([]byte{byte('0' + x%10)}, s...)
	}
	if n == 0 {
		s = []byte{'0'}
	}
	rotated := make([]byte, len(s))
	for i := 0; i < len(s); i++ {
		ch := s[len(s)-1-i]
		r, ok := rotate[ch]
		if !ok {
			return false
		}
		rotated[i] = r
	}
	return string(rotated) != string(s)
}
