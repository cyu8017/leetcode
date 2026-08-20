// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

import "strings"

func largestEven(s string) string {
	return strings.TrimRight(s, "1")
}
