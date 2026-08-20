// LeetCode 2289 - Steps to Make Array Non-decreasing
// https://leetcode.com/problems/steps-to-make-array-non-decreasing/

func totalSteps(nums []int) int {
	type pair struct{ val, steps int }
	stack := []pair{}
	ans := 0
	for i := len(nums) - 1; i >= 0; i-- {
		steps := 0
		for len(stack) > 0 && nums[i] > stack[len(stack)-1].val {
			if stack[len(stack)-1].steps > steps {
				steps = stack[len(stack)-1].steps
			}
			stack = stack[:len(stack)-1]
			steps++
		}
		if steps > ans {
			ans = steps
		}
		stack = append(stack, pair{nums[i], steps})
	}
	return ans
}
