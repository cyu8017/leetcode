// LeetCode 2743 - Count Substrings Without Repeating Character
// https://leetcode.com/problems/count-substrings-without-repeating-character/


func numberOfSpecialSubstrings(s string) int {
	last := [26]int{}
	for i := range last {
		last[i] = -1
	}
	ans, left := 0, 0
	for right := 0; right < len(s); right++ {
		c := int(s[right] - 'a')
		if last[c] >= left {
			left = last[c] + 1
		}
		last[c] = right
		ans += right - left + 1
	}
	return ans
}
