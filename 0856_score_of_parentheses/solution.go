// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

func scoreOfParentheses(s string) int {
	stack := []int{0}
	for _, ch := range s {
		if ch == '(' {
			stack = append(stack, 0)
		} else {
			val := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			add := 2 * val
			if add < 1 {
				add = 1
			}
			stack[len(stack)-1] += add
		}
	}
	return stack[0]
}
