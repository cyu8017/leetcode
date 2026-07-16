// LeetCode 0507 - Perfect Number
// https://leetcode.com/problems/perfect-number/

func checkPerfectNumber(num int) bool {
	if num <= 1 {
		return false
	}
	total := 1
	for divisor := 2; divisor*divisor <= num; divisor++ {
		if num%divisor == 0 {
			total += divisor
			pair := num / divisor
			if pair != divisor {
				total += pair
			}
		}
	}
	return total == num
}
