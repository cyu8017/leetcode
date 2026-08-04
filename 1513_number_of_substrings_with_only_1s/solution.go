// LeetCode 1513 - Number of Substrings With Only 1s
// https://leetcode.com/problems/number-of-substrings-with-only-1s/

func numSub(s string) int {
	ans, run := 0, 0
	for _, ch := range s {
		if ch == '1' {
			run++
			ans += run
		} else {
			run = 0
		}
	}
	return ans % 1000000007
}
