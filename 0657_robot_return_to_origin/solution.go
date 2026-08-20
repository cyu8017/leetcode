// LeetCode 0657 - Robot Return to Origin
// https://leetcode.com/problems/robot-return-to-origin/

import "strings"

func judgeCircle(moves string) bool {
	return strings.Count(moves, "U") == strings.Count(moves, "D") &&
		strings.Count(moves, "L") == strings.Count(moves, "R")
}
