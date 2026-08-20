// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

func checkString(s string) bool {
	seenB := false
	for i := 0; i < len(s); i++ {
		if s[i] == 'b' {
			seenB = true
		} else if seenB {
			return false
		}
	}
	return true
}
