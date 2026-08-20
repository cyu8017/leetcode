// LeetCode 2810 - Faulty Keyboard
// https://leetcode.com/problems/faulty-keyboard/

func finalString(s string) string {
	var b []byte
	for i := 0; i < len(s); i++ {
		if s[i] == 'i' {
			for l, r := 0, len(b)-1; l < r; l, r = l+1, r-1 {
				b[l], b[r] = b[r], b[l]
			}
		} else {
			b = append(b, s[i])
		}
	}
	return string(b)
}
