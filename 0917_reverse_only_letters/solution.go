// LeetCode 0917 - Reverse Only Letters
// https://leetcode.com/problems/reverse-only-letters/

func reverseOnlyLetters(s string) string {
	chars := []byte(s)
	i, j := 0, len(chars)-1
	for i < j {
		for i < j && !isAlpha(chars[i]) {
			i++
		}
		for i < j && !isAlpha(chars[j]) {
			j--
		}
		chars[i], chars[j] = chars[j], chars[i]
		i++
		j--
	}
	return string(chars)
}

func isAlpha(b byte) bool {
	return (b >= 'a' && b <= 'z') || (b >= 'A' && b <= 'Z')
}
