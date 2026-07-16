// LeetCode 0496 - Next Greater Element I
// https://leetcode.com/problems/next-greater-element-i/

func nextGreaterElement(nums1 []int, nums2 []int) []int {
	nextGreater := map[int]int{}
	stack := []int{}
	for _, num := range nums2 {
		for len(stack) > 0 && stack[len(stack)-1] < num {
			nextGreater[stack[len(stack)-1]] = num
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, num)
	}
	result := make([]int, len(nums1))
	for index, num := range nums1 {
		value, ok := nextGreater[num]
		if !ok {
			value = -1
		}
		result[index] = value
	}
	return result
}
