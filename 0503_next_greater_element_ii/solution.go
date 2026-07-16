// LeetCode 0503 - Next Greater Element II
// https://leetcode.com/problems/next-greater-element-ii/

func nextGreaterElements(nums []int) []int {
	length := len(nums)
	result := make([]int, length)
	for index := range result {
		result[index] = -1
	}
	stack := []int{}

	for index := 0; index < length*2; index++ {
		value := nums[index%length]
		for len(stack) > 0 && nums[stack[len(stack)-1]] < value {
			target := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			result[target] = value
		}
		if index < length {
			stack = append(stack, index)
		}
	}
	return result
}
