// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

func reverseParentheses(s string) string {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] == ')' {
			chunk := []byte{}
			for len(stack) > 0 && stack[len(stack)-1] != '(' {
				chunk = append(chunk, stack[len(stack)-1])
				stack = stack[:len(stack)-1]
			}
			stack = stack[:len(stack)-1]
			stack = append(stack, chunk...)
		} else {
			stack = append(stack, s[i])
		}
	}
	return string(stack)
}
