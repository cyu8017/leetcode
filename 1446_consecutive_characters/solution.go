// LeetCode 1446 - Consecutive Characters
// https://leetcode.com/problems/consecutive-characters/

func maxPower(s string) int {
	answer, run := 1, 1
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			run++
		} else {
			run = 1
		}
		if run > answer {
			answer = run
		}
	}
	return answer
}
