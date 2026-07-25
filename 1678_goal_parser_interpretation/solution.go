// LeetCode 1678 - Goal Parser Interpretation
// https://leetcode.com/problems/goal-parser-interpretation/

import "strings"

func interpret(command string) string {
	command = strings.ReplaceAll(command, "()", "o")
	return strings.ReplaceAll(command, "(al)", "al")
}
