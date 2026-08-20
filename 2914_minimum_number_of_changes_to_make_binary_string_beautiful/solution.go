// LeetCode 2914 - Minimum Number of Changes to Make Binary String Beautiful
// https://leetcode.com/problems/minimum-number-of-changes-to-make-binary-string-beautiful/

func minChanges(s string) int {
	ans := 0
	for i := 0; i < len(s); i += 2 {
		if s[i] != s[i+1] {
			ans++
		}
	}
	return ans
}
