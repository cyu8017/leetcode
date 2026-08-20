// LeetCode 2535 - Difference Between Element Sum and Digit Sum of an Array
// https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

func differenceOfSum(nums []int) int {
	elem, digit := 0, 0
	for _, x := range nums {
		elem += x
		for x > 0 {
			digit += x % 10
			x /= 10
		}
	}
	if elem > digit {
		return elem - digit
	}
	return digit - elem
}
