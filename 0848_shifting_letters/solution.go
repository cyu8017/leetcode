// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

func shiftingLetters(s string, shifts []int) string {
	total := 0
	chars := []byte(s)
	for i := len(s) - 1; i >= 0; i-- {
		total = (total + shifts[i]) % 26
		chars[i] = byte((int(chars[i]-'a')+total)%26 + 'a')
	}
	return string(chars)
}
