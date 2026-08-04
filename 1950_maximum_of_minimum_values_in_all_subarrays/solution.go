// LeetCode 1950 - Maximum of Minimum Values in All Subarrays
// https://leetcode.com/problems/maximum-of-minimum-values-in-all-subarrays/

func findMaximums(nums []int) []int {
	n := len(nums)
	left := make([]int, n)
	right := make([]int, n)
	stack := []int{}
	for i, x := range nums {
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= x {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			left[i] = -1
		} else {
			left[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	stack = stack[:0]
	for i := n - 1; i >= 0; i-- {
		for len(stack) > 0 && nums[stack[len(stack)-1]] >= nums[i] {
			stack = stack[:len(stack)-1]
		}
		if len(stack) == 0 {
			right[i] = n
		} else {
			right[i] = stack[len(stack)-1]
		}
		stack = append(stack, i)
	}
	ans := make([]int, n)
	for i, x := range nums {
		length := right[i] - left[i] - 1
		if x > ans[length-1] {
			ans[length-1] = x
		}
	}
	for i := n - 2; i >= 0; i-- {
		if ans[i+1] > ans[i] {
			ans[i] = ans[i+1]
		}
	}
	return ans
}
