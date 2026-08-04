// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

func longestPrefix(s string) string {
	if len(s) == 0 {
		return ""
	}
	pi := make([]int, len(s))
	for i := 1; i < len(s); i++ {
		j := pi[i-1]
		for j > 0 && s[i] != s[j] {
			j = pi[j-1]
		}
		if s[i] == s[j] {
			j++
		}
		pi[i] = j
	}
	return s[:pi[len(s)-1]]
}
