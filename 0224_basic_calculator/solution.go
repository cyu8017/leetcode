// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

func calculate(s string) int {
	stack := []int{}
	result := 0
	number := 0
	sign := 1
	for _, ch := range s {
		switch {
		case ch >= '0' && ch <= '9':
			number = number*10 + int(ch-'0')
		case ch == '+' || ch == '-':
			result += sign * number
			number = 0
			if ch == '+' {
				sign = 1
			} else {
				sign = -1
			}
		case ch == '(':
			stack = append(stack, result)
			stack = append(stack, sign)
			result = 0
			sign = 1
		case ch == ')':
			result += sign * number
			number = 0
			result *= stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result += stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
	}
	result += sign * number
	return result
}
