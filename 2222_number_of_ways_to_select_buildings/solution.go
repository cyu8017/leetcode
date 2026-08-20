// LeetCode 2222 - Number of Ways to Select Buildings
// https://leetcode.com/problems/number-of-ways-to-select-buildings/

func numberOfWays(s string) int64 {
	n := len(s)
	total0, total1 := 0, 0
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			total0++
		} else {
			total1++
		}
	}
	left0, left1 := 0, 0
	var ans int64
	for i := 0; i < n; i++ {
		if s[i] == '0' {
			ans += int64(left1) * int64(total1-left1)
			left0++
		} else {
			ans += int64(left0) * int64(total0-left0)
			left1++
		}
	}
	return ans
}
