// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

func decodeAtIndex(s string, k int) string {
	size := 0
	for i := 0; i < len(s); i++ {
		if s[i] >= '0' && s[i] <= '9' {
			size *= int(s[i] - '0')
		} else {
			size++
		}
	}
	for i := len(s) - 1; i >= 0; i-- {
		ch := s[i]
		k %= size
		if k == 0 && ch >= 'a' && ch <= 'z' {
			return string(ch)
		}
		if ch >= '0' && ch <= '9' {
			size /= int(ch - '0')
		} else {
			size--
		}
	}
	return ""
}
