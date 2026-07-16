// LeetCode 0392 - Is Subsequence
// https://leetcode.com/problems/is-subsequence/

func isSubsequence(s string, t string) bool {
	index := 0
	for _, ch := range t {
		if index < len(s) && s[index] == byte(ch) {
			index++
		}
	}
	return index == len(s)
}
