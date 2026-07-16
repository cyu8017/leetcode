// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

func calculate(s string) int {
	stack := []int{}
	number := 0
	operator := byte('+')

	for index := 0; index < len(s); index++ {
		ch := s[index]
		if ch >= '0' && ch <= '9' {
			number = number*10 + int(ch-'0')
		}
		if ch == '+' || ch == '-' || ch == '*' || ch == '/' || index == len(s)-1 {
			switch operator {
			case '+':
				stack = append(stack, number)
			case '-':
				stack = append(stack, -number)
			case '*':
				prev := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				stack = append(stack, prev*number)
			case '/':
				prev := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				stack = append(stack, prev/number)
			}
			operator = ch
			number = 0
		}
	}

	total := 0
	for _, value := range stack {
		total += value
	}
	return total
}
