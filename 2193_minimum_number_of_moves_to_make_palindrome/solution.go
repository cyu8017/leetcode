// LeetCode 2193 - Minimum Number of Moves to Make Palindrome
// https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/

func minMovesToMakePalindrome(s string) int {
	b := []byte(s)
	ans := 0
	for len(b) > 1 {
		j := len(b) - 1
		for j > 0 && b[j] != b[0] {
			j--
		}
		if j == 0 {
			// odd center
			ans += len(b) / 2
			b = b[1:]
			continue
		}
		ans += len(b) - 1 - j
		b = append(b[:j], b[j+1:]...)
		b = b[1 : len(b)-1]
	}
	return ans
}
