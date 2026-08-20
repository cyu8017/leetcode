// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

func toLowerCase(s string) string {
	b := []byte(s)
	for i, ch := range b {
		if ch >= 'A' && ch <= 'Z' {
			b[i] = ch + 32
		}
	}
	return string(b)
}
