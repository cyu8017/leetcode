// LeetCode 1904 - The Number of Full Rounds You Have Played
// https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/

func numberOfRounds(loginTime string, logoutTime string) int {
	toMin := func(t string) int {
		h := int(t[0]-'0')*10 + int(t[1]-'0')
		m := int(t[3]-'0')*10 + int(t[4]-'0')
		return h*60 + m
	}
	start, end := toMin(loginTime), toMin(logoutTime)
	if end < start {
		end += 24 * 60
	}
	start = (start + 14) / 15 * 15
	end = end / 15 * 15
	if end-start < 0 {
		return 0
	}
	return (end - start) / 15
}
