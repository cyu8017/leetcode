// LeetCode 2454 - Next Greater Element IV
// https://leetcode.com/problems/next-greater-element-iv/

func secondGreaterElement(nums []int) []int {
	n := len(nums)
	ans := make([]int, n)
	for i := range ans {
		ans[i] = -1
	}
	stack1, stack2 := []int{}, []int{}
	for i, x := range nums {
		for len(stack2) > 0 && nums[stack2[len(stack2)-1]] < x {
			ans[stack2[len(stack2)-1]] = x
			stack2 = stack2[:len(stack2)-1]
		}
		tmp := []int{}
		for len(stack1) > 0 && nums[stack1[len(stack1)-1]] < x {
			tmp = append(tmp, stack1[len(stack1)-1])
			stack1 = stack1[:len(stack1)-1]
		}
		for j := len(tmp) - 1; j >= 0; j-- {
			stack2 = append(stack2, tmp[j])
		}
		stack1 = append(stack1, i)
	}
	return ans
}
