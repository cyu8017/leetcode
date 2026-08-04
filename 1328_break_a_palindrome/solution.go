// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

func breakPalindrome(palindrome string) string {
	if len(palindrome) == 1 {
		return ""
	}
	chars := []byte(palindrome)
	for i := 0; i < len(chars)/2; i++ {
		if chars[i] != 'a' {
			chars[i] = 'a'
			return string(chars)
		}
	}
	chars[len(chars)-1] = 'b'
	return string(chars)
}
