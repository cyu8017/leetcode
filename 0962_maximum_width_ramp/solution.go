// LeetCode 0962 - Maximum Width Ramp
// https://leetcode.com/problems/maximum-width-ramp/

func maxWidthRamp(nums []int) int {
	stack := []int{}
	for i, x := range nums {
		if len(stack) == 0 || nums[stack[len(stack)-1]] > x {
			stack = append(stack, i)
		}
	}
	ans := 0
	for j := len(nums) - 1; j >= 0; j-- {
		for len(stack) > 0 && nums[stack[len(stack)-1]] <= nums[j] {
			diff := j - stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if diff > ans {
				ans = diff
			}
		}
	}
	return ans
}
