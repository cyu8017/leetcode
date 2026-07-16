// LeetCode 0054 - Spiral Matrix
// https://leetcode.com/problems/spiral-matrix/

func spiralOrder(matrix [][]int) []int {
	if len(matrix) == 0 {
		return []int{}
	}

	top := 0
	bottom := len(matrix) - 1
	left := 0
	right := len(matrix[0]) - 1
	result := make([]int, 0, len(matrix)*len(matrix[0]))

	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			result = append(result, matrix[top][col])
		}
		top++

		for row := top; row <= bottom; row++ {
			result = append(result, matrix[row][right])
		}
		right--

		if top <= bottom {
			for col := right; col >= left; col-- {
				result = append(result, matrix[bottom][col])
			}
			bottom--
		}

		if left <= right {
			for row := bottom; row >= top; row-- {
				result = append(result, matrix[row][left])
			}
			left++
		}
	}

	return result
}
