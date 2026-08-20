// LeetCode 0639 - Decode Ways II
// https://leetcode.com/problems/decode-ways-ii/

func numDecodings(s string) int {
	const mod = 1000000007
	one := func(ch byte) int {
		if ch == '*' {
			return 9
		}
		if ch == '0' {
			return 0
		}
		return 1
	}
	two := func(a, b byte) int {
		if a == '*' && b == '*' {
			return 15
		}
		if a == '*' {
			if b <= '6' {
				return 2
			}
			return 1
		}
		if b == '*' {
			if a == '1' {
				return 9
			}
			if a == '2' {
				return 6
			}
			return 0
		}
		value := int(a-'0')*10 + int(b-'0')
		if value >= 10 && value <= 26 {
			return 1
		}
		return 0
	}
	prev2, prev1 := 1, one(s[0])
	for i := 1; i < len(s); i++ {
		cur := (one(s[i])*prev1 + two(s[i-1], s[i])*prev2) % mod
		prev2, prev1 = prev1, cur
	}
	return prev1
}
