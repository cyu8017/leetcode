// LeetCode 0739 - Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/

func dailyTemperatures(temperatures []int) []int {
	answer := make([]int, len(temperatures))
	stack := []int{}
	for i, temp := range temperatures {
		for len(stack) > 0 && temperatures[stack[len(stack)-1]] < temp {
			prev := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			answer[prev] = i - prev
		}
		stack = append(stack, i)
	}
	return answer
}
