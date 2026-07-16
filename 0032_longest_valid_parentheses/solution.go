// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

func longestValidParentheses(s string) int {
	stack := []int{-1}
	best := 0

	for i, ch := range s {
		if ch == '(' {
			stack = append(stack, i)
		} else {
			stack = stack[:len(stack)-1]
			if len(stack) == 0 {
				stack = append(stack, i)
			} else {
				if length := i - stack[len(stack)-1]; length > best {
					best = length
				}
			}
		}
	}

	return best
}
