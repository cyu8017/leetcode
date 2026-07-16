// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

import "strings"

func parseTernary(expression string) string {
	if !strings.ContainsRune(expression, '?') {
		return expression
	}

	separator := 2
	depth := 0
	for index := 2; index < len(expression); index++ {
		switch expression[index] {
		case '?':
			depth++
		case ':':
			if depth == 0 {
				separator = index
				index = len(expression)
			} else {
				depth--
			}
		}
	}

	if expression[0] == 'T' {
		return parseTernary(expression[2:separator])
	}
	return parseTernary(expression[separator+1:])
}
