// LeetCode 2315 - Count Asterisks
// https://leetcode.com/problems/count-asterisks/

func countAsterisks(s string) int {
	ans := 0
	inside := false
	for i := 0; i < len(s); i++ {
		if s[i] == '|' {
			inside = !inside
		} else if s[i] == '*' && !inside {
			ans++
		}
	}
	return ans
}
