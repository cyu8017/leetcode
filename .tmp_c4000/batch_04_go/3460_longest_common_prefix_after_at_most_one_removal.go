// LeetCode 3460 - Longest Common Prefix After At Most One Removal
// https://leetcode.com/problems/longest-common-prefix-after-at-most-one-removal/

func longestCommonPrefix(s string, t string) int {
	i, j, removed := 0, 0, false
	for i < len(s) && j < len(t) {
		if s[i] == t[j] {
			i++
			j++
			continue
		}
		if removed {
			break
		}
		// remove from s
		removed = true
		i++
	}
	return j
}
