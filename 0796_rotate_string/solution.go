// LeetCode 0796 - Rotate String
// https://leetcode.com/problems/rotate-string/

import "strings"

func rotateString(s string, goal string) bool {
	return len(s) == len(goal) && strings.Contains(s+s, goal)
}
