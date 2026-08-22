// LeetCode 3933 - Largest Local Values in a Matrix II
// https://leetcode.com/problems/largest-local-values-in-a-matrix-ii/

func countLocalMaximums(matrix [][]int) int {
	rows, cols := len(matrix), len(matrix[0])
	positions := make([][][2]int, 201)
	for row := 0; row < rows; row++ {
		for col, value := range matrix[row] {
			if value > 0 {
				positions[value] = append(positions[value], [2]int{row, col})
			}
		}
	}

	answer := 0
	for value := 1; value <= 200; value++ {
		if len(positions[value]) == 0 {
			continue
		}
		prefix := make([][]int, rows+1)
		for i := range prefix {
			prefix[i] = make([]int, cols+1)
		}
		for row := 0; row < rows; row++ {
			for col := 0; col < cols; col++ {
				add := 0
				if matrix[row][col] > value {
					add = 1
				}
				prefix[row+1][col+1] = prefix[row][col+1] + prefix[row+1][col] - prefix[row][col] + add
			}
		}
		for _, position := range positions[value] {
			row, col := position[0], position[1]
			top, bottom := max3933(0, row-value), min3933(rows-1, row+value)
			left, right := max3933(0, col-value), min3933(cols-1, col+value)
			greater := prefix[bottom+1][right+1] - prefix[top][right+1] -
				prefix[bottom+1][left] + prefix[top][left]
			for _, dr := range []int{-value, value} {
				for _, dc := range []int{-value, value} {
					r, c := row+dr, col+dc
					if r >= 0 && r < rows && c >= 0 && c < cols && matrix[r][c] > value {
						greater--
					}
				}
			}
			if greater == 0 {
				answer++
			}
		}
	}
	return answer
}

func min3933(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max3933(a, b int) int {
	if a > b {
		return a
	}
	return b
}