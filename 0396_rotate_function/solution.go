// LeetCode 0396 - Rotate Function
// https://leetcode.com/problems/rotate-function/

func maxRotateFunction(nums []int) int {
	total := 0
	current := 0
	for index, value := range nums {
		total += value
		current += index * value
	}

	best := current
	for index := len(nums) - 1; index > 0; index-- {
		current += total - len(nums)*nums[index]
		if current > best {
			best = current
		}
	}

	return best
}
