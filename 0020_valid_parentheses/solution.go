// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

func isValid(s string) bool {
	stack := make([]byte, 0, len(s))
	pairs := map[byte]byte{
		')': '(',
		']': '[',
		'}': '{',
	}

	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' || ch == '[' || ch == '{' {
			stack = append(stack, ch)
		} else if len(stack) == 0 || stack[len(stack)-1] != pairs[ch] {
			return false
		} else {
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}
