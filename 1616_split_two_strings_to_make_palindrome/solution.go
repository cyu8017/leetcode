// LeetCode 1616 - Split Two Strings to Make Palindrome
// https://leetcode.com/problems/split-two-strings-to-make-palindrome/

func checkPalindromeFormation(a string, b string) bool {
	return check1616(a, b) || check1616(b, a)
}

func check1616(x, y string) bool {
	i, j := 0, len(x)-1
	for i < j && x[i] == y[j] {
		i++
		j--
	}
	return isPal1616(x[i:j+1]) || isPal1616(y[i:j+1])
}

func isPal1616(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
