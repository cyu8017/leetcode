// LeetCode 1309 - Decrypt String from Alphabet to Integer Mapping
// https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

func freqAlphabets(s string) string {
	var chars []byte
	i := len(s) - 1
	for i >= 0 {
		if s[i] == '#' {
			n := int(s[i-2]-'0')*10 + int(s[i-1]-'0')
			chars = append(chars, byte(96+n))
			i -= 3
		} else {
			chars = append(chars, byte(96+int(s[i]-'0')))
			i--
		}
	}
	for l, r := 0, len(chars)-1; l < r; l, r = l+1, r-1 {
		chars[l], chars[r] = chars[r], chars[l]
	}
	return string(chars)
}
