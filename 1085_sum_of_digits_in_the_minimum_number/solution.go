// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

func sumOfDigits(nums []int) int {
	n := nums[0]
	for _, x := range nums[1:] {
		if x < n {
			n = x
		}
	}
	digitSum := 0
	for n > 0 {
		digitSum += n % 10
		n /= 10
	}
	if digitSum%2 == 0 {
		return 1
	}
	return 0
}
