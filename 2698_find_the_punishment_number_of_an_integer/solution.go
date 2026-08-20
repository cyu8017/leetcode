// LeetCode 2698 - Find the Punishment Number of an Integer
// https://leetcode.com/problems/find-the-punishment-number-of-an-integer/


func punishmentNumber(n int) int {
	var canPartition func(s string, target int) bool
	canPartition = func(s string, target int) bool {
		if target < 0 {
			return false
		}
		if s == "" {
			return target == 0
		}
		val := 0
		for i := 0; i < len(s); i++ {
			val = val*10 + int(s[i]-'0')
			if canPartition(s[i+1:], target-val) {
				return true
			}
		}
		return false
	}
	ans := 0
	for i := 1; i <= n; i++ {
		sq := i * i
		s := ""
		for x := sq; x > 0; x /= 10 {
			s = string(byte('0'+x%10)) + s
		}
		if canPartition(s, i) {
			ans += sq
		}
	}
	return ans
}
