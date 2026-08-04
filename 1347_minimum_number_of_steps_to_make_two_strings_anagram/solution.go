// LeetCode 1347 - Minimum Number of Steps to Make Two Strings Anagram
// https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

func minSteps(s string, t string) int {
	count := [26]int{}
	for i := 0; i < len(s); i++ {
		count[s[i]-'a']++
		count[t[i]-'a']--
	}
	answer := 0
	for _, c := range count {
		if c > 0 {
			answer += c
		}
	}
	return answer
}
