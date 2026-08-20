// LeetCode 2553 - Separate the Digits in an Array
// https://leetcode.com/problems/separate-the-digits-in-an-array/


func separateDigits(nums []int) []int {
	ans := []int{}
	for _, x := range nums {
		digits := []int{}
		for x > 0 {
			digits = append(digits, x%10)
			x /= 10
		}
		for i := len(digits) - 1; i >= 0; i-- {
			ans = append(ans, digits[i])
		}
	}
	return ans
}
