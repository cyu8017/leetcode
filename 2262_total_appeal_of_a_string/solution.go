// LeetCode 2262 - Total Appeal of A String
// https://leetcode.com/problems/total-appeal-of-a-string/

func appealSum(s string) int64 {
	last := make([]int, 26)
	for i := range last {
		last[i] = -1
	}
	var ans int64
	var cur int64
	for i := 0; i < len(s); i++ {
		c := int(s[i] - 'a')
		cur += int64(i - last[c])
		last[c] = i
		ans += cur
	}
	return ans
}
