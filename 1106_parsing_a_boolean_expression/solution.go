// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

func parseBoolExpr(expression string) bool {
	stack := []byte{}
	for i := 0; i < len(expression); i++ {
		ch := expression[i]
		if ch == ')' {
			values := []bool{}
			for len(stack) > 0 && stack[len(stack)-1] != '&' && stack[len(stack)-1] != '|' && stack[len(stack)-1] != '!' {
				token := stack[len(stack)-1]
				stack = stack[:len(stack)-1]
				if token == 't' || token == 'f' {
					values = append(values, token == 't')
				}
			}
			op := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			var result bool
			if op == '!' {
				result = !values[0]
			} else if op == '&' {
				result = true
				for _, v := range values {
					result = result && v
				}
			} else {
				result = false
				for _, v := range values {
					result = result || v
				}
			}
			if result {
				stack = append(stack, 't')
			} else {
				stack = append(stack, 'f')
			}
		} else if ch != ',' {
			stack = append(stack, ch)
		}
	}
	return stack[len(stack)-1] == 't'
}
