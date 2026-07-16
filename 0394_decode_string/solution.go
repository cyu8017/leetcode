// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

import "strings"

func decodeString(s string) string {
	stack := make([][2]interface{}, 0)
	current := strings.Builder{}
	number := 0

	for _, ch := range s {
		switch {
		case ch >= '0' && ch <= '9':
			number = number*10 + int(ch-'0')
		case ch == '[':
			stack = append(stack, [2]interface{}{current.String(), number})
			current.Reset()
			number = 0
		case ch == ']':
			entry := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			previous := entry[0].(string)
			count := entry[1].(int)
			repeated := strings.Repeat(current.String(), count)
			current.Reset()
			current.WriteString(previous)
			current.WriteString(repeated)
		default:
			current.WriteRune(ch)
		}
	}

	return current.String()
}
