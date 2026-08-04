// LeetCode 1422 - Maximum Score After Splitting a String
// https://leetcode.com/problems/maximum-score-after-splitting-a-string/

func maxScore(s string) int {
	ones := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			ones++
		}
	}
	leftZeros, answer := 0, 0
	for i := 0; i < len(s)-1; i++ {
		if s[i] == '0' {
			leftZeros++
		} else {
			ones--
		}
		if leftZeros+ones > answer {
			answer = leftZeros + ones
		}
	}
	return answer
}
