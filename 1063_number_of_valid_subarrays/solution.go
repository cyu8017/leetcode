// LeetCode 1063 - Number of Valid Subarrays
// https://leetcode.com/problems/number-of-valid-subarrays/

func validSubarrays(nums []int) int {
	stack := []int{}
	ans := 0
	for i, x := range nums {
		for len(stack) > 0 && nums[stack[len(stack)-1]] > x {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ans += i - j
		}
		stack = append(stack, i)
	}
	for len(stack) > 0 {
		j := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		ans += len(nums) - j
	}
	return ans
}
