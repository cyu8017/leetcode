// LeetCode 0091 - Decode Ways
// https://leetcode.com/problems/decode-ways/

func numDecodings(s string) int {
	if len(s) == 0 || s[0] == '0' {
		return 0
	}

	prev2 := 1
	prev1 := 1

	for i := 1; i < len(s); i++ {
		current := 0
		if s[i] != '0' {
			current += prev1
		}
		two := int(s[i-1]-'0')*10 + int(s[i]-'0')
		if two >= 10 && two <= 26 {
			current += prev2
		}
		prev2, prev1 = prev1, current
	}

	return prev1
}
