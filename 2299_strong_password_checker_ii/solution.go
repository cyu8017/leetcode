// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

func strongPasswordCheckerII(password string) bool {
	if len(password) < 8 {
		return false
	}
	special := "!@#$%^&*()-+"
	hasLower, hasUpper, hasDigit, hasSpecial := false, false, false, false
	for i := 0; i < len(password); i++ {
		c := password[i]
		if i > 0 && c == password[i-1] {
			return false
		}
		if c >= 'a' && c <= 'z' {
			hasLower = true
		} else if c >= 'A' && c <= 'Z' {
			hasUpper = true
		} else if c >= '0' && c <= '9' {
			hasDigit = true
		} else {
			for j := 0; j < len(special); j++ {
				if c == special[j] {
					hasSpecial = true
					break
				}
			}
		}
	}
	return hasLower && hasUpper && hasDigit && hasSpecial
}
