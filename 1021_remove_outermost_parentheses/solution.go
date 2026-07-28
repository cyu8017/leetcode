// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

func removeOuterParentheses(s string) string {
	ans := make([]byte, 0, len(s))
	depth := 0
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' {
			if depth > 0 {
				ans = append(ans, ch)
			}
			depth++
		} else {
			depth--
			if depth > 0 {
				ans = append(ans, ch)
			}
		}
	}
	return string(ans)
}
