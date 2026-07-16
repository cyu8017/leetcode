// LeetCode 0360 - Sort Transformed Array
// https://leetcode.com/problems/sort-transformed-array/

func sortTransformedArray(nums []int, a int, b int, c int) []int {
	transform := func(value int) int {
		return a*value*value + b*value + c
	}

	left := 0
	right := len(nums) - 1
	result := make([]int, len(nums))
	index := len(nums) - 1
	step := -1
	if a <= 0 {
		index = 0
		step = 1
	}

	for left <= right {
		leftValue := transform(nums[left])
		rightValue := transform(nums[right])

		if a > 0 {
			if leftValue > rightValue {
				result[index] = leftValue
				left++
			} else {
				result[index] = rightValue
				right--
			}
		} else if leftValue < rightValue {
			result[index] = leftValue
			left++
		} else {
			result[index] = rightValue
			right--
		}

		index += step
	}

	return result
}
