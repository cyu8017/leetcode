// LeetCode 2544 - Alternating Digit Sum
// https://leetcode.com/problems/alternating-digit-sum/


func alternateDigitSum(n int) int {
	s := []int{}
	for n > 0 {
		s = append(s, n%10)
		n /= 10
	}
	ans, sign := 0, 1
	for i := len(s) - 1; i >= 0; i-- {
		ans += sign * s[i]
		sign = -sign
	}
	return ans
}
