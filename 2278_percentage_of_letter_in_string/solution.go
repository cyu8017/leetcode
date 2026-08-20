// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

func percentageLetter(s string, letter byte) int {
	cnt := 0
	for i := 0; i < len(s); i++ {
		if s[i] == letter {
			cnt++
		}
	}
	return cnt * 100 / len(s)
}
