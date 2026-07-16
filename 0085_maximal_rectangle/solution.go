// LeetCode 0085 - Maximal Rectangle
// https://leetcode.com/problems/maximal-rectangle/

func largestHistogram(heights []int) int {
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

func maximalRectangle(matrix [][]byte) int {
	if len(matrix) == 0 {
		return 0
	}

	cols := len(matrix[0])
	heights := make([]int, cols)
	maxArea := 0

	for _, row := range matrix {
		for j := 0; j < cols; j++ {
			if row[j] == '1' {
				heights[j]++
			} else {
				heights[j] = 0
			}
		}
		area := largestHistogram(heights)
		if area > maxArea {
			maxArea = area
		}
	}

	return maxArea
}
