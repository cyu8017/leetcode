// LeetCode 2697 - Lexicographically Smallest Palindrome
// https://leetcode.com/problems/lexicographically-smallest-palindrome/


func makeSmallestPalindrome(s string) string {
	b := []byte(s)
	l, r := 0, len(b)-1
	for l < r {
		if b[l] != b[r] {
			if b[l] < b[r] {
				b[r] = b[l]
			} else {
				b[l] = b[r]
			}
		}
		l++
		r--
	}
	return string(b)
}
