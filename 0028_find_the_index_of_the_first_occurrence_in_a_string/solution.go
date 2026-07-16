// LeetCode 0028 - Find the Index of the First Occurrence in a String
// https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	needleLen := len(needle)
	for i := 0; i <= len(haystack)-needleLen; i++ {
		if haystack[i:i+needleLen] == needle {
			return i
		}
	}
	return -1
}
