// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

import "strings"

func checkOnesSegment(s string) bool {
	trimmed := strings.Trim(s, "0")
	return !strings.Contains(trimmed, "01")
}
