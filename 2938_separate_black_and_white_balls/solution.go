// LeetCode 2938 - Separate Black and White Balls
// https://leetcode.com/problems/separate-black-and-white-balls/

func minimumSteps(s string) int64 {
	var ans, zeros int64
	for i := len(s) - 1; i >= 0; i-- {
		if s[i] == '0' {
			zeros++
		} else {
			ans += zeros
		}
	}
	return ans
}
