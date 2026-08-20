// LeetCode 2566 - Maximum Difference by Remapping a Digit
// https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/


func minMaxDifference(num int) int {
	s := []byte{}
	for x := num; x > 0; x /= 10 {
		s = append([]byte{byte('0' + x%10)}, s...)
	}
	if len(s) == 0 {
		s = []byte{'0'}
	}
	remap := func(from, to byte) int {
		v := 0
		for _, c := range s {
			d := c
			if d == from {
				d = to
			}
			v = v*10 + int(d-'0')
		}
		return v
	}
	maxV := num
	for _, c := range s {
		if c != '9' {
			maxV = remap(c, '9')
			break
		}
	}
	minV := remap(s[0], '0')
	return maxV - minV
}
