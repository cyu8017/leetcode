// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

func reversePrefix(s string, k int) string {
	t := []byte(s[:k])
	slices.Reverse(t)
	return string(t) + s[k:]
}
