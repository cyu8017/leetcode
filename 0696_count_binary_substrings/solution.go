// LeetCode 0696 - Count Binary Substrings
// https://leetcode.com/problems/count-binary-substrings/

func countBinarySubstrings(s string) int {
	prev, cur, ans := 0, 1, 0
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			cur++
		} else {
			ans += min(prev, cur)
			prev = cur
			cur = 1
		}
	}
	return ans + min(prev, cur)
}
