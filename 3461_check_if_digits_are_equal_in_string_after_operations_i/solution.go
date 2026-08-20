// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

func hasSameDigits(s string) bool {
	b := []byte(s)
	for len(b) > 2 {
		nb := make([]byte, len(b)-1)
		for i := 0; i+1 < len(b); i++ {
			nb[i] = byte('0' + (int(b[i]-'0')+int(b[i+1]-'0'))%10)
		}
		b = nb
	}
	return b[0] == b[1]
}
