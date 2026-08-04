// LeetCode 1544 - Make The String Great
// https://leetcode.com/problems/make-the-string-great/

func makeGood(s string) string {
	stack := []byte{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if len(stack) > 0 {
			top := stack[len(stack)-1]
			if top != ch && (top|32) == (ch|32) {
				stack = stack[:len(stack)-1]
				continue
			}
		}
		stack = append(stack, ch)
	}
	return string(stack)
}
