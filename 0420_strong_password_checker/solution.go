// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

import "unicode"

func strongPasswordChecker(password string) int {
	length := len(password)
	missing := 3
	hasLower, hasUpper, hasDigit := false, false, false

	for _, ch := range password {
		switch {
		case unicode.IsLower(ch):
			hasLower = true
		case unicode.IsUpper(ch):
			hasUpper = true
		case unicode.IsDigit(ch):
			hasDigit = true
		}
	}
	if hasLower {
		missing--
	}
	if hasUpper {
		missing--
	}
	if hasDigit {
		missing--
	}

	replace := 0
	oneRepeat := 0
	twoRepeat := 0
	index := 0
	for index < length {
		run := 1
		for index+run < length && password[index+run] == password[index] {
			run++
		}
		if run >= 3 {
			replace += run / 3
			switch run % 3 {
			case 0:
				oneRepeat++
			case 1:
				twoRepeat++
			}
		}
		index += run
	}

	if length < 6 {
		return max(6-length, missing)
	}
	if length <= 20 {
		return max(missing, replace)
	}

	deleteCount := length - 20
	replace -= min(deleteCount, oneRepeat)
	deleteCount -= min(deleteCount, oneRepeat)
	replace -= min(deleteCount/2, twoRepeat)
	deleteCount -= min(deleteCount/2, twoRepeat) * 2
	replace -= deleteCount / 3
	return length - 20 + max(missing, replace)
}
