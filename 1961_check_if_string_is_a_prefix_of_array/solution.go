// LeetCode 1961 - Check If String Is a Prefix of Array
// https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

func isPrefixString(s string, words []string) bool {
	cur := ""
	for _, w := range words {
		cur += w
		if cur == s {
			return true
		}
		if len(cur) > len(s) || s[:len(cur)] != cur {
			return false
		}
	}
	return false
}
