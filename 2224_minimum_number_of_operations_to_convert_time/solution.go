// LeetCode 2224 - Minimum Number of Operations to Convert Time
// https://leetcode.com/problems/minimum-number-of-operations-to-convert-time/

func convertTime(current string, correct string) int {
	toMin := func(t string) int {
		return int(t[0]-'0')*600 + int(t[1]-'0')*60 + int(t[3]-'0')*10 + int(t[4]-'0')
	}
	diff := toMin(correct) - toMin(current)
	ans := 0
	for _, step := range []int{60, 15, 5, 1} {
		ans += diff / step
		diff %= step
	}
	return ans
}
