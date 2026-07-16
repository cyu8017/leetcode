// LeetCode 0084 - Largest Rectangle in Histogram
// https://leetcode.com/problems/largest-rectangle-in-histogram/

func largestRectangleArea(heights []int) int {
	stack := make([]int, 0)
	maxArea := 0
	extended := append(append([]int{}, heights...), 0)

	for i, height := range extended {
		for len(stack) > 0 && extended[stack[len(stack)-1]] > height {
			h := extended[stack[len(stack)-1]]
			stack = stack[:len(stack)-1]
			width := i
			if len(stack) > 0 {
				width = i - stack[len(stack)-1] - 1
			}
			area := h * width
			if area > maxArea {
				maxArea = area
			}
		}
		stack = append(stack, i)
	}

	return maxArea
}
