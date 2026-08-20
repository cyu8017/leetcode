// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

func checkValidString(s string) bool {
	lo, hi := 0, 0
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if ch == '(' {
			lo++
			hi++
		} else if ch == ')' {
			if lo > 0 {
				lo--
			}
			hi--
			if hi < 0 {
				return false
			}
		} else {
			if lo > 0 {
				lo--
			}
			hi++
		}
	}
	return lo == 0
}
