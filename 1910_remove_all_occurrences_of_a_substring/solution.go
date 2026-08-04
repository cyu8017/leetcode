// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

func removeOccurrences(s string, part string) string {
	stack := make([]byte, 0, len(s))
	m := len(part)
	for i := 0; i < len(s); i++ {
		stack = append(stack, s[i])
		if len(stack) >= m {
			match := true
			for j := 0; j < m; j++ {
				if stack[len(stack)-m+j] != part[j] {
					match = false
					break
				}
			}
			if match {
				stack = stack[:len(stack)-m]
			}
		}
	}
	return string(stack)
}
