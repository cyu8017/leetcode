// LeetCode 0521 - Longest Uncommon Subsequence I
// https://leetcode.com/problems/longest-uncommon-subsequence-i/

func findLUSlength(a string, b string) int {
	if a != b {
		if len(a) > len(b) {
			return len(a)
		}
		return len(b)
	}
	return -1
}
