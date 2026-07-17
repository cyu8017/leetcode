// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

func replaceDigits(s string) string {
	chars := []byte(s)
	for i := 1; i < len(chars); i += 2 {
		chars[i] = chars[i-1] + (chars[i] - '0')
	}
	return string(chars)
}
