// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

func sequentialDigits(low int, high int) []int {
	digits := "123456789"
	answer := []int{}
	for length := 2; length <= 9; length++ {
		for start := 0; start <= 9-length; start++ {
			value := 0
			for i := start; i < start+length; i++ {
				value = value*10 + int(digits[i]-'0')
			}
			if value >= low && value <= high {
				answer = append(answer, value)
			}
		}
	}
	return answer
}
