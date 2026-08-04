// LeetCode 1427 - Perform String Shifts
// https://leetcode.com/problems/perform-string-shifts/

func stringShift(s string, shift [][]int) string {
	offset := 0
	for _, sh := range shift {
		if sh[0] == 1 {
			offset += sh[1]
		} else {
			offset -= sh[1]
		}
	}
	n := len(s)
	offset %= n
	if offset < 0 {
		offset += n
	}
	if offset == 0 {
		return s
	}
	return s[n-offset:] + s[:n-offset]
}
