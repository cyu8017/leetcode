// LeetCode 1221 - Split a String in Balanced Strings
// https://leetcode.com/problems/split-a-string-in-balanced-strings/

func balancedStringSplit(s string) int {
	balance, answer := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == 'L' {
			balance++
		} else {
			balance--
		}
		if balance == 0 {
			answer++
		}
	}
	return answer
}
