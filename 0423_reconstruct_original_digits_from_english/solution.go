// LeetCode 0423 - Reconstruct Original Digits from English
// https://leetcode.com/problems/reconstruct-original-digits-from-english/

import "strings"

func originalDigits(s string) string {
	counts := make(map[byte]int)
	for i := 0; i < len(s); i++ {
		counts[s[i]]++
	}

	digitCounts := make([]int, 10)
	digitCounts[0] = counts['z']
	digitCounts[2] = counts['w']
	digitCounts[4] = counts['u']
	digitCounts[6] = counts['x']
	digitCounts[8] = counts['g']
	digitCounts[1] = counts['o'] - digitCounts[0] - digitCounts[2] - digitCounts[4]
	digitCounts[3] = counts['h'] - digitCounts[8]
	digitCounts[5] = counts['f'] - digitCounts[4]
	digitCounts[7] = counts['s'] - digitCounts[6]
	digitCounts[9] = counts['i'] - digitCounts[5] - digitCounts[6] - digitCounts[8]

	var builder strings.Builder
	for digit := 0; digit < 10; digit++ {
		for count := 0; count < digitCounts[digit]; count++ {
			builder.WriteByte(byte('0' + digit))
		}
	}
	return builder.String()
}
