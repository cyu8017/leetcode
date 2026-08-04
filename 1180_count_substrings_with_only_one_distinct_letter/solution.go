// LeetCode 1180 - Count Substrings with Only One Distinct Letter
// https://leetcode.com/problems/count-substrings-with-only-one-distinct-letter/

func countLetters(s string) int {
	ans, length := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			length++
		} else {
			length = 1
		}
		ans += length
	}
	return ans
}
