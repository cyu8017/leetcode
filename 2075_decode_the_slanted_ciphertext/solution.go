// LeetCode 2075 - Decode the Slanted Ciphertext
// https://leetcode.com/problems/decode-the-slanted-ciphertext/

import "strings"

func decodeCiphertext(encodedText string, rows int) string {
	if rows == 1 {
		return encodedText
	}
	cols := len(encodedText) / rows
	var b strings.Builder
	for c := 0; c < cols; c++ {
		for r := 0; r < rows && c+r < cols; r++ {
			b.WriteByte(encodedText[r*cols+c+r])
		}
	}
	return strings.TrimRight(b.String(), " ")
}
