// LeetCode 1432 - Max Difference You Can Get From Changing an Integer
// https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/

import "strconv"
import "strings"

func maxDiff(num int) int {
	s := strconv.Itoa(num)
	high := s
	for i := 0; i < len(s); i++ {
		if s[i] != '9' {
			high = strings.ReplaceAll(s, string(s[i]), "9")
			break
		}
	}
	low := s
	if s[0] != '1' {
		low = strings.ReplaceAll(s, string(s[0]), "1")
	} else {
		for i := 1; i < len(s); i++ {
			if s[i] != '0' && s[i] != '1' {
				low = strings.ReplaceAll(s, string(s[i]), "0")
				break
			}
		}
	}
	h, _ := strconv.Atoi(high)
	l, _ := strconv.Atoi(low)
	return h - l
}
