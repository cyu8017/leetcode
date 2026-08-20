// LeetCode 0926 - Flip String to Monotone Increasing
// https://leetcode.com/problems/flip-string-to-monotone-increasing/

func minFlipsMonoIncr(s string) int {
	ones, ans := 0, 0
	for _, ch := range s {
		if ch == '1' {
			ones++
		} else {
			if ans+1 < ones {
				ans = ans + 1
			} else {
				ans = ones
			}
		}
	}
	return ans
}
