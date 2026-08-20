// LeetCode 2696 - Minimum String Length After Removing Substrings
// https://leetcode.com/problems/minimum-string-length-after-removing-substrings/


func minLength(s string) int {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		c := s[i]
		if len(stack) > 0 {
			top := stack[len(stack)-1]
			if (top == 'A' && c == 'B') || (top == 'C' && c == 'D') {
				stack = stack[:len(stack)-1]
				continue
			}
		}
		stack = append(stack, c)
	}
	return len(stack)
}
