// LeetCode 1758 - Minimum Changes To Make Alternating Binary String
// https://leetcode.com/problems/minimum-changes-to-make-alternating-binary-string/

func minOperations(s string) int {
	alt1 := 0
	for i := 0; i < len(s); i++ {
		expected := byte('0')
		if i&1 == 1 {
			expected = '1'
		}
		if s[i] != expected {
			alt1++
		}
	}
	if alt1 < len(s)-alt1 {
		return alt1
	}
	return len(s) - alt1
}
