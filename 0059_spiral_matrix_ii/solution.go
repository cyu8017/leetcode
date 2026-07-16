// LeetCode 0059 - Spiral Matrix II
// https://leetcode.com/problems/spiral-matrix-ii/

func generateMatrix(n int) [][]int {
	matrix := make([][]int, n)
	for i := range matrix {
		matrix[i] = make([]int, n)
	}

	top := 0
	bottom := n - 1
	left := 0
	right := n - 1
	num := 1

	for top <= bottom && left <= right {
		for col := left; col <= right; col++ {
			matrix[top][col] = num
			num++
		}
		top++

		for row := top; row <= bottom; row++ {
			matrix[row][right] = num
			num++
		}
		right--

		if top <= bottom {
			for col := right; col >= left; col-- {
				matrix[bottom][col] = num
				num++
			}
			bottom--
		}

		if left <= right {
			for row := bottom; row >= top; row-- {
				matrix[row][left] = num
				num++
			}
			left++
		}
	}

	return matrix
}
