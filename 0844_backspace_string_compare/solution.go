// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

func backspaceCompare(s string, t string) bool {
	build := func(text string) string {
		stack := []byte{}
		for i := 0; i < len(text); i++ {
			if text[i] == '#' {
				if len(stack) > 0 {
					stack = stack[:len(stack)-1]
				}
			} else {
				stack = append(stack, text[i])
			}
		}
		return string(stack)
	}
	return build(s) == build(t)
}
