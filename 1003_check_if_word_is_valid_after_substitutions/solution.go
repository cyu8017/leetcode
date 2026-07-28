// LeetCode 1003 - Check If Word Is Valid After Substitutions
// https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/

func isValid(s string) bool {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		stack = append(stack, s[i])
		for len(stack) >= 3 && stack[len(stack)-3] == 'a' && stack[len(stack)-2] == 'b' && stack[len(stack)-1] == 'c' {
			stack = stack[:len(stack)-3]
		}
	}
	return len(stack) == 0
}
