// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

func calculate(s string) int {
	expr := make([]byte, 0, len(s))
	for i := 0; i < len(s); i++ {
		if s[i] != ' ' {
			expr = append(expr, s[i])
		}
	}
	var parse func(int) (int, int)
	parse = func(i int) (int, int) {
		stack := []int{}
		num := 0
		sign := byte('+')
		for i < len(expr) {
			ch := expr[i]
			if ch >= '0' && ch <= '9' {
				num = num*10 + int(ch-'0')
			}
			if ch == '(' {
				num, i = parse(i + 1)
			}
			if ch == '+' || ch == '-' || ch == '*' || ch == '/' || ch == ')' || i == len(expr)-1 {
				if sign == '+' {
					stack = append(stack, num)
				} else if sign == '-' {
					stack = append(stack, -num)
				} else if sign == '*' {
					stack[len(stack)-1] *= num
				} else {
					top := stack[len(stack)-1]
					stack[len(stack)-1] = top / num
				}
				if ch == ')' {
					sum := 0
					for _, v := range stack {
						sum += v
					}
					return sum, i
				}
				sign = ch
				num = 0
			}
			i++
		}
		sum := 0
		for _, v := range stack {
			sum += v
		}
		return sum, i
	}
	ans, _ := parse(0)
	return ans
}
