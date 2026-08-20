// LeetCode 2380 - Time Needed to Rearrange a Binary String
// https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/

func secondsToRemoveOccurrences(s string) int {
	ans, zeros := 0, 0
	for i := 0; i < len(s); i++ {
		if s[i] == '0' {
			zeros++
		} else if zeros > 0 {
			if ans+1 > zeros {
				ans = ans + 1
			} else {
				ans = zeros
			}
		}
	}
	return ans
}
