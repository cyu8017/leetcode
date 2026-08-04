// LeetCode 1944 - Number of Visible People in a Queue
// https://leetcode.com/problems/number-of-visible-people-in-a-queue/

func canSeePersonsCount(heights []int) []int {
	n := len(heights)
	ans := make([]int, n)
	stack := []int{}
	for i := n - 1; i >= 0; i-- {
		count := 0
		for len(stack) > 0 && heights[i] > stack[len(stack)-1] {
			stack = stack[:len(stack)-1]
			count++
		}
		if len(stack) > 0 {
			count++
		}
		ans[i] = count
		stack = append(stack, heights[i])
	}
	return ans
}
