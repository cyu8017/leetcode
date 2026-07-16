// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

func productExceptSelf(nums []int) []int {
	length := len(nums)
	result := make([]int, length)
	prefix := 1
	for index := 0; index < length; index++ {
		result[index] = prefix
		prefix *= nums[index]
	}
	suffix := 1
	for index := length - 1; index >= 0; index-- {
		result[index] *= suffix
		suffix *= nums[index]
	}
	return result
}
