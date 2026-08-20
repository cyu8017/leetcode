// LeetCode 2381 - Shifting Letters II
// https://leetcode.com/problems/shifting-letters-ii/

func shiftingLetters(s string, shifts [][]int) string {
	n := len(s)
	diff := make([]int, n+1)
	for _, sh := range shifts {
		d := 1
		if sh[2] == 0 {
			d = -1
		}
		diff[sh[0]] += d
		diff[sh[1]+1] -= d
	}
	b := []byte(s)
	cur := 0
	for i := 0; i < n; i++ {
		cur = (cur + diff[i]) % 26
		if cur < 0 {
			cur += 26
		}
		b[i] = byte('a' + (int(b[i]-'a')+cur)%26)
	}
	return string(b)
}
