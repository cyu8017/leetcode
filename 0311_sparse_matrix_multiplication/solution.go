// LeetCode 0311 - Sparse Matrix Multiplication
// https://leetcode.com/problems/sparse-matrix-multiplication/

func multiply(mat1 [][]int, mat2 [][]int) [][]int {
	rows := len(mat1)
	inner := len(mat1[0])
	cols := len(mat2[0])
	result := make([][]int, rows)
	for row := 0; row < rows; row++ {
		result[row] = make([]int, cols)
		for index := 0; index < inner; index++ {
			if mat1[row][index] == 0 {
				continue
			}
			for col := 0; col < cols; col++ {
				if mat2[index][col] != 0 {
					result[row][col] += mat1[row][index] * mat2[index][col]
				}
			}
		}
	}
	return result
}
