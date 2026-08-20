// LeetCode 3295 - Report Spam Message
// https://leetcode.com/problems/report-spam-message/

func reportSpam(message []string, bannedWords []string) bool {
	ban := map[string]bool{}
	for _, w := range bannedWords {
		ban[w] = true
	}
	cnt := 0
	for _, w := range message {
		if ban[w] {
			cnt++
			if cnt >= 2 {
				return true
			}
		}
	}
	return false
}
