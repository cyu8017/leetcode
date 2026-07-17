// LeetCode 1750 - Minimum Length of String After Deleting Similar Ends
// https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

func minimumLength(s string) int {
	left := 0
	right := len(s) - 1
	for left < right && s[left] == s[right] {
		ch := s[left]
		for left <= right && s[left] == ch {
			left++
		}
		for left <= right && s[right] == ch {
			right--
		}
	}
	return right - left + 1
}
