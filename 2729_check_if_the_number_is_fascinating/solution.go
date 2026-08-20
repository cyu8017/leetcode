// LeetCode 2729 - Check if The Number is Fascinating
// https://leetcode.com/problems/check-if-the-number-is-fascinating/


import "strconv"

func isFascinating(n int) bool {
	s := strconv.Itoa(n) + strconv.Itoa(2*n) + strconv.Itoa(3*n)
	if len(s) != 9 {
		return false
	}
	seen := [10]bool{}
	for i := 0; i < len(s); i++ {
		d := int(s[i] - '0')
		if d == 0 || seen[d] {
			return false
		}
		seen[d] = true
	}
	return true
}
