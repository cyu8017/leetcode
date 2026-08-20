// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

func smallestFactorization(num int) int {
	if num < 10 {
		return num
	}
	digits := []int{}
	for digit := 9; digit >= 2; digit-- {
		for num%digit == 0 {
			digits = append(digits, digit)
			num /= digit
		}
	}
	if num != 1 {
		return 0
	}
	result := 0
	for i := len(digits) - 1; i >= 0; i-- {
		result = result*10 + digits[i]
		if result > 1<<31-1 {
			return 0
		}
	}
	return result
}
