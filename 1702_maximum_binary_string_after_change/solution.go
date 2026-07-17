// LeetCode 1702 - Maximum Binary String After Change
// https://leetcode.com/problems/maximum-binary-string-after-change/

import "strings"

func maximumBinaryString(binary string) string {
	zeros := strings.Count(binary, "0")
	if zeros <= 1 {
		return binary
	}
	first := strings.IndexByte(binary, '0')
	n := len(binary)
	return strings.Repeat("1", first+zeros-1) + "0" + strings.Repeat("1", n-first-zeros)
}
